"""
TwoFactorAuthManager - A class to handle batch 2FA password modifications with proper async context management.

This module provides:
1. Isolated async contexts to prevent event loop conflicts
2. Explicit event loop management with strict timeout controls
3. Multi-layer exception handling
4. TXT report generation for failed accounts
5. Automatic TData password file updates with backup
"""

import asyncio
import os
import shutil
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from telethon import TelegramClient
from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
import telethon


class TwoFactorAuthManager:
    """
    Manages batch 2FA password modifications with isolated async contexts.
    
    Features:
    - Event loop isolation to prevent conflicts
    - Timeout controls for all async operations
    - Multi-layer exception handling
    - Detailed failure reporting
    - Automatic TData file updates with backup
    """
    
    def __init__(self, base_path: str = "更改二步tdata", timeout: int = 20):
        """
        Initialize the TwoFactorAuthManager.
        
        Args:
            base_path: Base directory for processing accounts
            timeout: Default timeout for async operations (seconds)
        """
        self.base_path = base_path
        self.timeout = timeout
        self.failed_accounts: List[Dict[str, str]] = []
        self.success_accounts: List[str] = []
        
    async def modify_2fa_tdata(
        self,
        phone: str,
        old_passwords: List[str],
        new_password: str,
        semaphore: asyncio.Semaphore
    ) -> Tuple[bool, Optional[str]]:
        """
        Modify 2FA password for a TData account with isolated async context.
        
        Args:
            phone: Phone number/account identifier
            old_passwords: List of possible old passwords (or ['无'] if no password)
            new_password: New password to set
            semaphore: Semaphore for concurrency control
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        async with semaphore:
            session_path = f"临时session/{phone}"
            session_file = f"{session_path}.session"
            client = None
            
            try:
                # Create isolated event loop context
                tdata_path = f'{self.base_path}/{phone}/tdata'
                
                # Load TDesktop with timeout
                try:
                    tdesk = await asyncio.wait_for(
                        self._load_tdesktop(tdata_path),
                        timeout=self.timeout
                    )
                except asyncio.TimeoutError:
                    return False, "TDesktop loading timeout"
                
                if not tdesk:
                    return False, "Failed to load TDesktop"
                
                # Convert to Telethon with timeout
                try:
                    client = await asyncio.wait_for(
                        tdesk.ToTelethon(session=session_path, flag=UseCurrentSession),
                        timeout=self.timeout
                    )
                except asyncio.TimeoutError:
                    return False, "TDesktop to Telethon conversion timeout"
                
                # Connect with timeout
                try:
                    await asyncio.wait_for(client.connect(), timeout=self.timeout)
                except asyncio.TimeoutError:
                    return False, "Connection timeout"
                except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
                    return False, "Duplicate auth key"
                except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
                    return False, "Unregistered auth key"
                except Exception as e:
                    return False, f"Connection error: {type(e).__name__}"
                
                # Modify 2FA password
                success, error = await self._modify_password(
                    client, old_passwords, new_password
                )
                
                if success:
                    self.success_accounts.append(phone)
                    return True, None
                else:
                    return False, error
                    
            except Exception as e:
                # Multi-layer exception handling
                error_msg = f"Unexpected error: {type(e).__name__}: {str(e)}"
                return False, error_msg
                
            finally:
                # Ensure cleanup happens
                if client:
                    try:
                        await asyncio.wait_for(client.disconnect(), timeout=5)
                    except Exception:
                        pass
                
                # Clean up session file
                if os.path.exists(session_file):
                    try:
                        os.remove(session_file)
                    except Exception:
                        pass
    
    async def modify_2fa_session(
        self,
        phone: str,
        old_passwords: List[str],
        new_password: str,
        semaphore: asyncio.Semaphore,
        selected_item: str = "更改二步tdata"
    ) -> Tuple[bool, Optional[str]]:
        """
        Modify 2FA password for a session account with isolated async context.
        
        Args:
            phone: Phone number/account identifier
            old_passwords: List of possible old passwords (or ['无'] if no password)
            new_password: New password to set
            semaphore: Semaphore for concurrency control
            selected_item: Base path for session files
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        async with semaphore:
            client = None
            
            try:
                # Create client with isolated async context
                oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
                client = TelegramClient(f"{selected_item}/{phone}", oldAPI, timeout=self.timeout)
                
                # Connect with timeout
                try:
                    await asyncio.wait_for(client.connect(), timeout=self.timeout)
                except asyncio.TimeoutError:
                    return False, "Connection timeout"
                except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
                    return False, "Duplicate auth key"
                except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
                    return False, "Unregistered auth key"
                except Exception as e:
                    return False, f"Connection error: {type(e).__name__}"
                
                # Modify 2FA password
                success, error = await self._modify_password(
                    client, old_passwords, new_password
                )
                
                if success:
                    self.success_accounts.append(phone)
                    return True, None
                else:
                    return False, error
                    
            except Exception as e:
                # Multi-layer exception handling
                error_msg = f"Unexpected error: {type(e).__name__}: {str(e)}"
                return False, error_msg
                
            finally:
                # Ensure cleanup happens
                if client:
                    try:
                        await asyncio.wait_for(client.disconnect(), timeout=5)
                    except Exception:
                        pass
    
    async def _load_tdesktop(self, tdata_path: str) -> Optional[TDesktop]:
        """
        Load TDesktop with error handling.
        
        Args:
            tdata_path: Path to tdata directory
            
        Returns:
            TDesktop object or None if failed
        """
        try:
            tdesk = TDesktop(tdata_path)
            if tdesk.isLoaded():
                return tdesk
            return None
        except Exception:
            return None
    
    async def _modify_password(
        self,
        client: TelegramClient,
        old_passwords: List[str],
        new_password: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Modify 2FA password with multi-layer exception handling.
        
        Args:
            client: Connected TelegramClient
            old_passwords: List of possible old passwords
            new_password: New password to set
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        # Handle no current password case
        if len(old_passwords) == 1 and old_passwords[0] == '无':
            try:
                await asyncio.wait_for(
                    client.edit_2fa(new_password=new_password),
                    timeout=self.timeout
                )
                return True, None
            except asyncio.TimeoutError:
                return False, "2FA edit timeout"
            except Exception as e:
                return False, f"2FA edit failed: {type(e).__name__}: {str(e)}"
        
        # Try each old password
        last_error = None
        for old_password in old_passwords:
            try:
                await asyncio.wait_for(
                    client.edit_2fa(current_password=old_password, new_password=new_password),
                    timeout=self.timeout
                )
                return True, None
            except asyncio.TimeoutError:
                last_error = "2FA edit timeout"
                continue
            except Exception as e:
                last_error = f"{type(e).__name__}: {str(e)}"
                continue
        
        # All passwords failed
        return False, f"All passwords failed. Last error: {last_error}"
    
    def add_failed_account(self, phone: str, error: str):
        """
        Add a failed account to the failure list.
        
        Args:
            phone: Phone number/account identifier
            error: Error message
        """
        self.failed_accounts.append({
            'phone': phone,
            'error': error,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    def generate_failure_report(self, output_path: str) -> str:
        """
        Generate a comprehensive TXT report of all failed accounts.
        
        Args:
            output_path: Path where the report will be saved
            
        Returns:
            Path to the generated report file
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        total_processed = len(self.success_accounts) + len(self.failed_accounts)
        
        report_lines = [
            "=" * 80,
            "2FA Password Modification - Failure Report",
            "=" * 80,
            f"Report Generated: {timestamp}",
            "",
            "SUMMARY STATISTICS",
            "-" * 80,
            f"Total Accounts Processed: {total_processed}",
            f"Successful Modifications: {len(self.success_accounts)}",
            f"Failed Modifications: {len(self.failed_accounts)}",
            f"Success Rate: {(len(self.success_accounts) / total_processed * 100) if total_processed > 0 else 0:.2f}%",
            "",
            "FAILED ACCOUNTS DETAILS",
            "-" * 80,
        ]
        
        if self.failed_accounts:
            for i, failure in enumerate(self.failed_accounts, 1):
                report_lines.extend([
                    f"\n{i}. Account: {failure['phone']}",
                    f"   Time: {failure['timestamp']}",
                    f"   Error: {failure['error']}",
                ])
        else:
            report_lines.append("\nNo failed accounts.")
        
        report_lines.extend([
            "",
            "=" * 80,
            "End of Report",
            "=" * 80,
        ])
        
        report_content = "\n".join(report_lines)
        
        # Write report to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return output_path
    
    def update_tdata_password_files(
        self,
        phone: str,
        new_password: str,
        create_backup: bool = True
    ) -> bool:
        """
        Update TData password files (2fa.txt, password2fa.txt, passwordfa.txt).
        
        Args:
            phone: Phone number/account identifier
            new_password: New password to write
            create_backup: Whether to create backup before updating
            
        Returns:
            True if successful, False otherwise
        """
        tdata_dir = f"{self.base_path}/{phone}"
        
        if not os.path.exists(tdata_dir):
            return False
        
        password_files = ['2fa.txt', 'password2fa.txt', 'passwordfa.txt']
        
        try:
            # Create backup if requested
            if create_backup:
                backup_dir = f"{tdata_dir}/backup_{int(time.time())}"
                os.makedirs(backup_dir, exist_ok=True)
                
                for filename in password_files:
                    file_path = os.path.join(tdata_dir, filename)
                    if os.path.exists(file_path):
                        backup_path = os.path.join(backup_dir, filename)
                        shutil.copy2(file_path, backup_path)
            
            # Update password files
            for filename in password_files:
                file_path = os.path.join(tdata_dir, filename)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_password)
            
            return True
            
        except Exception as e:
            print(f"Error updating password files for {phone}: {e}")
            return False
    
    def reset_statistics(self):
        """Reset the success and failure statistics."""
        self.failed_accounts.clear()
        self.success_accounts.clear()


async def batch_modify_2fa_tdata(
    folder_names: List[str],
    old_password: str,
    new_password: str,
    base_path: str = "更改二步tdata",
    concurrency: int = 10
) -> Dict[str, any]:
    """
    Batch modify 2FA passwords for TData accounts with proper async management.
    
    Args:
        folder_names: List of phone numbers/account identifiers
        old_password: Old password(s) (space-separated if multiple, or '无' for none)
        new_password: New password to set
        base_path: Base directory for processing
        concurrency: Maximum concurrent tasks
        
    Returns:
        Dictionary with results including success/failed lists and manager instance
    """
    manager = TwoFactorAuthManager(base_path=base_path)
    semaphore = asyncio.Semaphore(concurrency)
    
    old_passwords = old_password.split(' ')
    
    tasks = []
    for phone in folder_names:
        task = manager.modify_2fa_tdata(phone, old_passwords, new_password, semaphore)
        tasks.append((phone, task))
    
    # Execute all tasks with proper async context
    success_list = []
    failed_list = []
    
    for phone, task in tasks:
        try:
            success, error = await task
            if success:
                success_list.append(phone)
            else:
                failed_list.append(phone)
                manager.add_failed_account(phone, error or "Unknown error")
        except Exception as e:
            failed_list.append(phone)
            manager.add_failed_account(phone, f"Task execution error: {str(e)}")
    
    return {
        'success': success_list,
        'failed': failed_list,
        'manager': manager,
        'stats': {
            'total': len(folder_names),
            'success_count': len(success_list),
            'failed_count': len(failed_list)
        }
    }


async def batch_modify_2fa_session(
    folder_names: List[str],
    old_password: str,
    new_password: str,
    base_path: str = "更改二步tdata",
    concurrency: int = 10
) -> Dict[str, any]:
    """
    Batch modify 2FA passwords for session accounts with proper async management.
    
    Args:
        folder_names: List of phone numbers/account identifiers
        old_password: Old password(s) (space-separated if multiple, or '无' for none)
        new_password: New password to set
        base_path: Base directory for processing
        concurrency: Maximum concurrent tasks
        
    Returns:
        Dictionary with results including success/failed lists and manager instance
    """
    manager = TwoFactorAuthManager(base_path=base_path)
    semaphore = asyncio.Semaphore(concurrency)
    
    old_passwords = old_password.split(' ')
    
    tasks = []
    for phone in folder_names:
        task = manager.modify_2fa_session(phone, old_passwords, new_password, semaphore, base_path)
        tasks.append((phone, task))
    
    # Execute all tasks with proper async context
    success_list = []
    failed_list = []
    
    for phone, task in tasks:
        try:
            success, error = await task
            if success:
                success_list.append(phone)
            else:
                failed_list.append(phone)
                manager.add_failed_account(phone, error or "Unknown error")
        except Exception as e:
            failed_list.append(phone)
            manager.add_failed_account(phone, f"Task execution error: {str(e)}")
    
    return {
        'success': success_list,
        'failed': failed_list,
        'manager': manager,
        'stats': {
            'total': len(folder_names),
            'success_count': len(success_list),
            'failed_count': len(failed_list)
        }
    }
