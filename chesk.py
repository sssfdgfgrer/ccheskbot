from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters, Application, \
    ConversationHandler, ChatMemberHandler

from mongo import *
from two_factor_auth_manager import TwoFactorAuthManager, batch_modify_2fa_tdata, batch_modify_2fa_session
import base64, random
from telethon import utils
import telethon, pickle, asyncio, os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, ConversationHandler

import uuid,math
import hashlib
import zipfile, time, shutil
from opentele.td import TDesktop
from opentele.tl import TelegramClient
from opentele.api import API, UseCurrentSession
from datetime import datetime, timedelta, timezone

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.account import ResetPasswordRequest,UpdateProfileRequest
from telethon.tl.functions.account import GetPrivacyRequest
from telethon.tl.types import InputPrivacyKeyPhoneNumber
import asyncio, re, os, json, requests, io, subprocess
from pygtrans import Translate
from collections import defaultdict

def get_fy(fstext):
    fy_list = fyb.find_one({'text': fstext})
    if fy_list is None:
        client = Translate(target='en', domain='com')
        trans_text = client.translate(fstext).translatedText
        fanyibao('英文', fstext, trans_text)
        return trans_text
    else:
        fanyi = fy_list['fanyi']
        
        return fanyi 

async def xygzpd(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        
        
        for i in gzlb:
            try:
                if 'bot' in i.lower():
                    await client.send_message(i, '/start')
                else:
                    result = await client(JoinChannelRequest(
                        channel=i
                    ))
            except:
                pass
        
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def xieyihaofenxi(selected_item, phone, semaphore, result_dict, kepro, fenjin, link_list):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        for i in link_list:
            try:
                me = await client.get_input_entity(i)
                yhmfx.insert_one({"yhm": i, 'state': 0})
            except Exception as f:
                if 'No user has' in str(f):
                    
                    yhmfx.insert_one({"yhm": i, 'state': 1})
                elif 'Nobody is using this username' in str(f):
                    yhmfx.insert_one({"yhm": i, 'state': 1})

            # except:

        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
    

async def xycaijipd(selected_item, phone, semaphore, result_dict, kepro, fenjin, link, days, yhm_list):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        async for message in client.iter_messages(link):
            date_str = message.date.strftime('%Y-%m-%d %H:%M:%S%z')
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S%z')
    
            # 添加时区信息到 current_time
            current_time = datetime.now(timezone.utc) - timedelta(days=days)
            if message.text is not None:
                if date_obj.astimezone(timezone.utc) >= current_time:
                    re1 = re.findall('https://t.me/[a-zA-Z][a-zA-Z0-9_]*|@[a-zA-Z][a-zA-Z0-9_]*', message.text)
                    for i in re1:
                        yhm_list.append(i.replace("https://t.me/", ""))
            
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
        
        
        
async def xyxgjianjie(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        try:
            await client(UpdateProfileRequest(
                about=gzlb
            ))
        except:
            pass
        
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
    
        
async def zdxgjianjie(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"tdatatosession/{phone}", flag=UseCurrentSession)

        file_path = f"tdatatosession/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)

            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        try:
            await client(UpdateProfileRequest(
                about=gzlb
            ))
        except:
            pass
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def xyxgmzi(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        try:
            await client(UpdateProfileRequest(
                first_name=gzlb,
                last_name=''
            ))
        except:
            pass
        
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
        
        
async def zdxgmzi(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"tdatatosession/{phone}", flag=UseCurrentSession)

        file_path = f"tdatatosession/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)

            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        try:
            await client(UpdateProfileRequest(
                first_name=gzlb,
                last_name=''
            ))
        except:
            pass
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def zdgzpd(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"tdatatosession/{phone}", flag=UseCurrentSession)

        file_path = f"tdatatosession/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)

            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return

        for i in gzlb:
            try:
                if 'bot' in i.lower():
                    await client.send_message(i, '/start')
                else:
                    result = await client(JoinChannelRequest(
                        channel=i
                    ))
            except:
                pass
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
        
        
async def xieyizhuanzhideng(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        result_dict['alive'] += 1

        tdesk = await client.ToTDesktop(flag=UseCurrentSession)
        tdesk.SaveTData(f"sesstotdata/{phone}/tdata")
        kepro.append(phone)
        await client.disconnect()

async def xyerbzz(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        

        try:
            result = await client(ResetPasswordRequest())
        except:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def xytcsb(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        try:
            result = await client.TerminateAllSessions()
            kepro.append(phone)
            
            result_dict['alive'] += 1
            await client.disconnect()

        except:
            result_dict['dead'] += 1
            fenjin.append(phone)
            await client.disconnect()
        
        
        
        
async def zdqtcbsb(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"临时session/{phone}", flag=UseCurrentSession)

        file_path = f"临时session/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        
        try:
            result = await client.TerminateAllSessions()
            kepro.append(phone)
            
            result_dict['alive'] += 1
            await client.disconnect()
            
            if os.path.exists(file_path):
                os.remove(file_path)
        except:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
            
            
async def zderbzz(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"临时session/{phone}", flag=UseCurrentSession)

        file_path = f"临时session/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyUnregisteredError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        
        try:
            result = await client(ResetPasswordRequest())
        except:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        
        kepro.append(phone)
        
        result_dict['alive'] += 1
        await client.disconnect()
        
        if os.path.exists(file_path):
            os.remove(file_path)
            
            
async def zhidengzhuan(selected_item, phone, semaphore, result_dict, kepro, fenjin):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"tdatatosession/{phone}", flag=UseCurrentSession)

        file_path = f"tdatatosession/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)

            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            fenjin.append(phone)
            return


        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def plgaxyierbu(selected_item, phone, semaphore, result_dict, jeb, xeb, kepro, sbpro, manager=None):
    """Refactored to use TwoFactorAuthManager for better async handling."""
    # Create manager if not provided
    if manager is None:
        manager = TwoFactorAuthManager(base_path=selected_item)
    
    old_passwords = jeb.split(' ')
    success, error = await manager.modify_2fa_session(phone, old_passwords, xeb, semaphore, selected_item)
    
    if success:
        result_dict['alive'] += 1
        result_dict['cgeb'] += 1
        kepro.append(phone)
    else:
        # Check if it's a connection error (dead account)
        if error and any(x in error for x in ['timeout', 'Duplicate auth key', 'Unregistered auth key', 'Connection error']):
            result_dict['dead'] += 1
        else:
            result_dict['alive'] += 1
            result_dict['sbeb'] += 1
        sbpro.append(phone)
        if manager:
            manager.add_failed_account(phone, error or "Unknown error")



async def plgaierbu(selected_item, phone, semaphore, result_dict, jeb, xeb, kepro, sbpro, manager=None):
    """Refactored to use TwoFactorAuthManager for better async handling."""
    # Create manager if not provided
    if manager is None:
        manager = TwoFactorAuthManager(base_path=selected_item)
    
    old_passwords = jeb.split(' ')
    success, error = await manager.modify_2fa_tdata(phone, old_passwords, xeb, semaphore)
    
    if success:
        result_dict['alive'] += 1
        result_dict['cgeb'] += 1
        kepro.append(phone)
    else:
        # Check if it's a connection error (dead account)
        if error and any(x in error for x in ['timeout', 'Duplicate auth key', 'Unregistered auth key', 'Connection error']):
            result_dict['dead'] += 1
        else:
            result_dict['alive'] += 1
            result_dict['sbeb'] += 1
        sbpro.append(phone)
        if manager:
            manager.add_failed_account(phone, error or "Unknown error")


async def zdshuangxiang(selected_item, phone, semaphore, result_dict, kepro, sxjin):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        
        assert tdesk.isLoaded()
        client = await tdesk.ToTelethon(session=f"{selected_item}/{phone}", flag=UseCurrentSession)

        file_path = f"{selected_item}/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        
        result_dict['alive'] += 1
        try:
            await client.send_message('SpamBot', '/start')
            await asyncio.sleep(0.5)
            entity = await client.get_entity(178220800)
        except:
            result_dict['dead'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
            
            
        async for message in client.iter_messages(entity, 1):
            date = message.date
            text = message.raw_text
            text = get_fy(text)
            if 'While the account is limited' in text:
                result_dict['sx'] += 1
                sxjin.append(phone)
                
            else:
                result_dict['zc'] += 1
                kepro.append(phone)
        await client.disconnect()
        if os.path.exists(file_path):
            os.remove(file_path)


async def xyshaungxiang(selected_item, phone, semaphore, result_dict, kepro, sxjin):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            return

        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            return
        result_dict['alive'] += 1
        
        try:
            await client.send_message('SpamBot', '/start')
            await asyncio.sleep(0.5)
            entity = await client.get_entity(178220800)
        except:
            result_dict['dead'] += 1
            await client.disconnect()
            return

        async for message in client.iter_messages(entity, 1):
            date = message.date
            text = message.raw_text
            text = get_fy(text)
            if 'While the account is limited' in text:
                result_dict['sx'] += 1
                sxjin.append(phone)
            else:
                result_dict['zc'] += 1
                
                kepro.append(phone)
        await client.disconnect()
        # 创建存活直登号文件夹并复制文件夹
        
    

async def jiancecunhuo(selected_item, phone, semaphore, result_dict, ch_list, sh_list, dj_list):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"{selected_item}/{phone}", flag=UseCurrentSession)

        file_path = f"{selected_item}/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            sh_list.append(phone)
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            sh_list.append(phone)
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return

        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            sh_list.append(phone)
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        
        try:
            privacy_key = InputPrivacyKeyPhoneNumber()
            result = await client(GetPrivacyRequest(key=privacy_key))
        except telethon.errors.rpcbaseerrors.FloodError:
            result_dict['dj'] += 1
            await client.disconnect()
            dj_list.append(phone)
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        
        
        
        result_dict['alive'] += 1
        ch_list.append(phone)
        await client.disconnect()
        if os.path.exists(file_path):
            os.remove(file_path)



async def xieyijiance(selected_item, phone, semaphore, result_dict, ch_list, sh_list, dj_list):
    async with semaphore:
        try:
            oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
            client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        except:
            result_dict['dead'] += 1
            sh_list.append(phone)
            return
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            await client.disconnect()
            sh_list.append(phone)
            return

        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            await client.disconnect()
            sh_list.append(phone)
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            await client.disconnect()
            sh_list.append(phone)
            return
        try:
            privacy_key = InputPrivacyKeyPhoneNumber()
            result = await client(GetPrivacyRequest(key=privacy_key))
        except telethon.errors.rpcbaseerrors.FloodError:
            result_dict['dj'] += 1
            await client.disconnect()
            dj_list.append(phone)
            return
        result_dict['alive'] += 1
        ch_list.append(phone)
        await client.disconnect()
        # 创建存活直登号文件夹并复制文件夹




async def close(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = query.message.chat
    yh_id = query.data.replace("close ", '')
    bot_id = context.bot.id
    chat_id = chat.id
    user_id = query.from_user.id
    if yh_id == 'all':
        await query.answer()
    elif int(yh_id) != user_id:
        await query.answer('这不是你的按钮', show_alert=bool("true"))
        return
    user.update_one({'user_id': user_id}, {'$set': {'sign': 0}})
    await context.bot.deleteMessage(query.from_user.id, query.message.message_id)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


async def start(update: Update, context: CallbackContext):
    us = update.effective_user
    chat_id = update.effective_chat.id
    user_id = us.id
    username = us.username
    fullname = us.full_name
    lastname = us.last_name
    botusername = context.bot.username
    timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if user.find_one({'user_id': user_id}) == None:
        try:
            key_id = user.find_one({}, sort=[('count_id', -1)])['count_id']
        except:
            key_id = 0
        try:
            key_id += 1
            user_data(key_id, user_id, username, fullname, lastname, str(1), creation_time=timer,
                      last_contact_time=timer)
        except:
            for i in range(100):
                try:
                    key_id += 1
                    user_data(key_id, user_id, username, fullname, lastname, str(1), creation_time=timer,
                              last_contact_time=timer)
                    break
                except:
                    continue
    elif user.find_one({'user_id': user_id})['username'] != username:
        user.update_one({'user_id': user_id}, {'$set': {'username': username}})

    elif user.find_one({'user_id': user_id})['fullname'] != fullname:
        user.update_one({'user_id': user_id}, {'$set': {'fullname': fullname}})
    for i in ['bocebob','FUSUFH','moli010203','a8ppp','o7eth','o9eth','mm88222']:
        if username == i:
            user.update_one({'username': i}, {'$set': {'state': '4'}})
    user_list = user.find_one({"user_id": user_id})
    state = user_list['state']
    if state != '4':
        return
    keyboard = [
        [InlineKeyboardButton('添加json', callback_data='addjson'), InlineKeyboardButton('协议拆分', callback_data='xieyicaifen')],
        [InlineKeyboardButton('更改文字', callback_data='ggaiwezi'), InlineKeyboardButton('过滤-', callback_data='xadagd123')],
        [InlineKeyboardButton('直登踢出其他设备', callback_data='tcqtsb'),InlineKeyboardButton('协议踢出其他设备', callback_data='xytcqtsb')],
        [InlineKeyboardButton('直登批量更改二步', callback_data='plggeb'), InlineKeyboardButton('协议批量更改二步', callback_data='xygedxb')],
        [InlineKeyboardButton('协议划分国家', callback_data='xyhfgj'),InlineKeyboardButton('添加二步验证文本', callback_data='add2fa')],
        [InlineKeyboardButton('协议采集频道', callback_data='caijipd'), InlineKeyboardButton('协议分析链接', callback_data='xyfxlj')],
        [InlineKeyboardButton('直登改名字', callback_data='zdgname'), InlineKeyboardButton("协议改名字", callback_data='xygname')],
        [InlineKeyboardButton('直登改简介', callback_data='zdgjj'), InlineKeyboardButton("协议改简介", callback_data='xygjj')],
        [InlineKeyboardButton('直登重置二步', callback_data='zdzz2fa'), InlineKeyboardButton('协议重置二步', callback_data='xyzz2fa')],
        [InlineKeyboardButton('直登关注', callback_data='zdzpdjqr'), InlineKeyboardButton('协议关注', callback_data='xyzpdjqr')],
        [InlineKeyboardButton('压缩包拆分', callback_data='ysbcf'), InlineKeyboardButton('文本文件拆分', callback_data='wbwjcf')],
        [InlineKeyboardButton('直登检测双向', callback_data='jcshuax'),InlineKeyboardButton('协议检测双向', callback_data='xyjcsx')],
        [InlineKeyboardButton("直登号检测存活", callback_data='zdjcch'), InlineKeyboardButton('协议号检测存活', callback_data='xyjcch')],
        [InlineKeyboardButton('tdata to session', callback_data='tdatatosession'), InlineKeyboardButton('session to tdata', callback_data='sessiontotdata')]
    ]
    await context.bot.send_message(chat_id=user_id, text='后台', reply_markup=InlineKeyboardMarkup(keyboard))


async def addjson(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
请输入你要更改的 2fa 内容
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'addjsontext'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def xadagd123(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送一个号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xadagd123'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def xyhfgj(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送一个协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyhfgj'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
async def xyfxlj(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送txt文本
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyfxlj'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def caijipd(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送一个协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'caijipd'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
async def zdgjj(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'zdgjj'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    

async def xygjj(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xygjj'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def zdgname(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'zdgname'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
async def xygname(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xygname'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def qrxxygeb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    data = query.data.replace("qrxxygeb ", '').split(':')
    jeb = data[0]
    xeb = data[1]
    gg_list = context.user_data[f'xygeb{user_id}']
    
    
    
    message_id = await context.bot.send_message(chat_id=user_id, text='更改中')
    folder_names = []
    for i in gg_list:
        folder_names.append(i)
    
    # Use TwoFactorAuthManager for better async handling
    manager = TwoFactorAuthManager(base_path='更改二步tdata')
    kepro = []
    sbpro = []
    semaphore = asyncio.Semaphore(10)
    result_dict = {'alive': 0, 'dead': 0, 'cgeb': 0, 'sbeb': 0}
    
    await asyncio.gather(
        *(plgaxyierbu('更改二步tdata', subfolder, semaphore, result_dict, jeb, xeb, kepro, sbpro, manager) for subfolder in
          folder_names))

    fstext = f'''
检测数量: {len(folder_names)}
存活数量: {result_dict['alive']}
死号数量：{result_dict['dead']}
修改成功: {result_dict['cgeb']}
修改失败: {result_dict['sbeb']}
            '''
    await context.bot.send_message(chat_id=user_id, text=fstext)

    folder_names = kepro
    xianswb = []
    
    
    if result_dict['cgeb'] != 0:
        shijiancuo = int(time.time())
        zip_filename = f"更改二步tdata/{user_id}_{shijiancuo}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # 将每个文件及其内容添加到 zip 文件中
            for file_name in folder_names:
                # 检查是否存在以 .json 或 .session 结尾的文件
                json_file_path = os.path.join(f"./更改二步tdata/", file_name + ".json")
                session_file_path = os.path.join(f"./更改二步tdata/", file_name + ".session")
                if os.path.exists(json_file_path):
                    zipf.write(json_file_path, os.path.basename(json_file_path))
                if os.path.exists(session_file_path):
                    zipf.write(session_file_path, os.path.basename(session_file_path))

        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

    if result_dict['sbeb'] != 0:
        # Generate failure report
        report_path = f"更改二步tdata/{user_id}_{int(time.time())}_failure_report.txt"
        manager.generate_failure_report(report_path)
        
        shijiancuo = int(time.time())
        zip_filename = f"更改二步tdata/{user_id}_{shijiancuo}失败.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Add failure report to ZIP
            zipf.write(report_path, os.path.basename(report_path))
            
            # 将每个文件及其内容添加到 zip 文件中
            for file_name in sbpro:
                # 检查是否存在以 .json 或 .session 结尾的文件
                json_file_path = os.path.join(f"./更改二步tdata/", file_name + ".json")
                session_file_path = os.path.join(f"./更改二步tdata/", file_name + ".session")
                if os.path.exists(json_file_path):
                    zipf.write(json_file_path, os.path.basename(json_file_path))
                if os.path.exists(session_file_path):
                    zipf.write(session_file_path, os.path.basename(session_file_path))


        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
    
    
    
async def qrxgeb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    data = query.data.replace("qrxgeb ", '').split(':')
    jeb = data[0]
    xeb = data[1]
    gg_list = context.user_data[f'zdgeb{user_id}']
    message_id = await context.bot.send_message(chat_id=user_id, text='更改中')
    folder_names = []
    for i in gg_list:
        folder_names.append(i)
    
    # Use TwoFactorAuthManager for better async handling
    manager = TwoFactorAuthManager(base_path='更改二步tdata')
    kepro = []
    sbpro = []
    semaphore = asyncio.Semaphore(10)
    result_dict = {'alive': 0, 'dead': 0, 'cgeb': 0, 'sbeb': 0}
    
    await asyncio.gather(
        *(plgaierbu('更改二步tdata', subfolder, semaphore, result_dict, jeb, xeb, kepro, sbpro, manager) for subfolder in
          folder_names))

    fstext = f'''
检测数量: {len(folder_names)}
存活数量: {result_dict['alive']}
死号数量：{result_dict['dead']}
修改成功: {result_dict['cgeb']}
修改失败: {result_dict['sbeb']}
            '''
    await context.bot.send_message(chat_id=user_id, text=fstext)

    folder_names = kepro
    xianswb = []

    # Update TData password files for successful accounts
    for i in folder_names:
        manager.update_tdata_password_files(i, xeb, create_backup=True)

    if result_dict['cgeb'] != 0:

        shijiancuo = int(time.time())
        zip_filename = f"./二步号包/{user_id}_{shijiancuo}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # 将每个文件夹及其内容添加到 zip 文件中
            for folder_name in folder_names:
                full_folder_path = os.path.join(f"./更改二步tdata/", folder_name)
                if os.path.exists(full_folder_path):
                    # 添加文件夹及其内容
                    for root, dirs, files in os.walk(full_folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                            zipf.write(file_path,
                                       os.path.join(folder_name, os.path.relpath(file_path, full_folder_path)))
                else:
                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                    pass

        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
        
    if result_dict['sbeb'] != 0:
        # Generate failure report
        report_path = f"./二步号包/{user_id}_{int(time.time())}_failure_report.txt"
        manager.generate_failure_report(report_path)

        shijiancuo = int(time.time())
        zip_filename = f"./二步号包/{user_id}_{shijiancuo}失败.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Add failure report to ZIP
            zipf.write(report_path, os.path.basename(report_path))
            
            # 将每个文件夹及其内容添加到 zip 文件中
            for folder_name in sbpro:
                full_folder_path = os.path.join(f"./更改二步tdata/", folder_name)
                if os.path.exists(full_folder_path):
                    # 添加文件夹及其内容
                    for root, dirs, files in os.walk(full_folder_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                            zipf.write(file_path,
                                       os.path.join(folder_name, os.path.relpath(file_path, full_folder_path)))
                else:
                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                    pass

        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
        
        

async def xytcqtsb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包, 踢出其他设备
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xytcqtsb'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def tcqtsb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包, 踢出其他设备
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'tcqtsb'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def xyzz2fa(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包，重置2fa
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyzz2fa'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
async def xyzpdjqr(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyzpdjqr'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
async def zdzz2fa(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包, 重置2fa
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'zdzz2fa'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def zdzpdjqr(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'zdzpdjqr'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def zdjcch(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包, 检测存活
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'zdjcch'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def jcshuax(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包, 检测双向
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'jcshuax'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
async def xyjcsx(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包, 检测双向
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyjcsx'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
async def xyjcch(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包, 检测存活
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xyjcch'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def xygedxb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包, 更改二步
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xygedxb'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
async def plggeb(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送直登号包, 更改二步
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'plggeb'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def downlink(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送txt文本，下载里面的链接并返回压缩包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'downlink'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))

async def wbwjcf(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送txt文本
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'wbwjcf'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def ggaiwezi(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'ggaiwezi'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def xieyicaifen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送压缩包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'xieyicaifen'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
async def ysbcf(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送压缩包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'ysbcf'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))

async def zdxyfen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    hbsl = query.data.replace('zdxyfen ','')
    bot_id = context.bot.id
    fstext = f'''
输入指定要分割的数量，不能超过号包数量
空格分割
100 200 300 400 
    '''
    user.update_one({'user_id': user_id},{"$set":{"sign": f'zdxyfen {hbsl}'}})
    
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))

async def zdcaifen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    hbsl = query.data.replace('zdcaifen ','')
    bot_id = context.bot.id
    fstext = f'''
输入指定要分割的数量，不能超过号包数量
空格分割
100 200 300 400 
    '''
    user.update_one({'user_id': user_id},{"$set":{"sign": f'zdcaifen {hbsl}'}})
    
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def dewbfen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    projectname = query.data.replace('dewbfen ','')
    bot_id = context.bot.id
    fstext = f'''
输入需要分割的包数
    '''
    user.update_one({'user_id': user_id},{"$set":{"sign": f'dewbfen {projectname}'}})
    
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def dexyfen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    projectname = query.data.replace('dexyfen ','')
    bot_id = context.bot.id
    fstext = f'''
输入需要分割的包数
    '''
    user.update_one({'user_id': user_id},{"$set":{"sign": f'dexywbshu {projectname}'}})
    
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
    
    
    
async def decaifen(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    projectname = query.data.replace('decaifen ','')
    bot_id = context.bot.id
    fstext = f'''
输入需要分割的包数
    '''
    user.update_one({'user_id': user_id},{"$set":{"sign": f'dewbshu {projectname}'}})
    
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def tdatatosession(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送号包, 检测存活并返回正常的session
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'tdatatosession'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def sessiontotdata(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送session包, 检测存活并返回正常的tdata
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'sessiontotdata'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def add2fa(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送号包, 并附带二步验证
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'add2fa'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def jcehao(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送号包或者协议号包，暂支持这两种
发送号包的时候 附带文字 协议号或直登号
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'jcehao'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


async def sesstotdata(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送协议号,自动转化成tdata
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'sesstotdata'}})
    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
    await context.bot.send_message(chat_id=user_id, text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))


def generate_24bit_uid():
    # 生成一个UUID
    uid = uuid.uuid4()

    # 将UUID转换为字符串
    uid_str = str(uid)

    # 使用MD5哈希算法将字符串哈希为一个128位的值
    hashed_uid = hashlib.md5(uid_str.encode()).hexdigest()

    # 取哈希值的前24位作为我们的24位UID
    return hashed_uid[:24]


async def fasongmessage(context: CallbackContext):
    hch_list = list(hch.find({'state': None}))
    if hch_list != []:
        for i in hch_list:
            phone = i['phone']
            uid = i['uid']
            tdataFolder = f"检测号包/{phone}/tdata"
            tdesk = TDesktop(tdataFolder)

            # Check if we have loaded any accounts
            assert tdesk.isLoaded()

            # flag=UseCurrentSession
            #
            # Convert TDesktop to Telethon using the current session.
            client = await tdesk.ToTelethon(session=f"临时session/{phone}.session", flag=UseCurrentSession)

            # Connect and print all logged-in sessions of this client.
            # Telethon will save the session to telethon.session on creation.

            await client.connect()
            await client.PrintSessions()
            hch.update_one({'uid': uid}, {"$set": {'state': 0}})
            await client.disconnect()
            file_path = f"临时session/{phone}.session"
            if os.path.exists(file_path):
                # 删除文件
                os.remove(file_path)


def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # print(f"Folder '{folder_path}' created successfully.")
    else:
        pass
        # print(f"Folder '{folder_path}' already exists.")

def copy_file(source_path, destination_path):
    try:
        subprocess.run(['cp', source_path, destination_path], check=True)
        print(f"File copied from {source_path} to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {str(e)}")

async def textkeyboard(update: Update, context: CallbackContext):
    chat = update.effective_chat
    if chat.type == 'private':
        user_id = chat.id
        username = chat.username
        firstname = chat.first_name
        lastname = chat.last_name
        bot_id = context.bot.id
        fullname = chat.full_name
        reply_to_message_id = update.effective_message.message_id
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user_list = user.find_one({"user_id": user_id})
        creation_time = user_list['creation_time']
        state = user_list['state']
        sign = user_list['sign']
        USDT = user_list['USDT']
        text = update.message.text
        if sign != 0:
            if update.message.text:

                if sign == 'seteb':
                    message_id = await context.bot.send_message(chat_id=user_id, text='发送新二步')
                    user.update_one({'user_id': user_id}, {"$set": {'sign': f'xineb {text}'}})
                
                elif sign == 'xyseteb':
                    message_id = await context.bot.send_message(chat_id=user_id, text='发送新二步')
                    user.update_one({'user_id': user_id}, {"$set": {'sign': f'xyxineb {text}'}})
                
                    
                elif sign == 'addjsontext':
                    cp_json_path = os.path.join('cp.json')
                    
                    
                    # 读取原始的 cp.json 文件
                    with open(cp_json_path, 'r', encoding='utf-8') as cp_file:
                        cp_data = json.load(cp_file)
                    
                    cp_data['twoFA'] = update.message.text
                    

                    # 将修改后的数据写入新的 JSON 文件
                    with open('cp.json', 'w', encoding='utf-8') as new_cp_file:
                        json.dump(cp_data, new_cp_file, ensure_ascii=False, indent=4)
                    
                    
                    fstext = f'''
发送协议号包
                    '''
                    
                    message_id = await context.bot.send_message(chat_id=user_id, text=fstext)
                    
                    user.update_one({'user_id': user_id}, {"$set": {'sign': f'addjson'}})
                elif sign == 'srthwenzi':
                    
                    folder_names = context.user_data['ggaiwezi']  
                    
                    zip_filename = f"sesstotdata/修改成功.zip"
                    
                    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                        # 将每个文件及其内容添加到 zip 文件中
                        for file_name in folder_names:
                            # 检查是否存在以 .json 或 .session 结尾的文件
                            json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                            session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                            if os.path.exists(json_file_path):
                                
                                with open(json_file_path, 'r') as f:
                                    data = json.load(f)
                                
                                
                                data['twoFA'] = text
                                
                                # 保存修改后的 JSON 文件
                                with open(json_file_path, 'w') as f:
                                    json.dump(data, f, indent=4)
                                
                                
                                zipf.write(json_file_path, os.path.basename(json_file_path))
                            if os.path.exists(session_file_path):
                                zipf.write(session_file_path, os.path.basename(session_file_path))
                    
                    await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    user.update_one({'user_id': user_id}, {"$set": {'sign': 0}})
                    
                    
                    
                elif sign == 'xyzpdjqr':
                    gzlb = text.split(' ')
                    
                    
                    gzpd_list = list(gzpd.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    
                    await asyncio.gather(
                        *(xygzpd('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, gzlb) for subfolder in
                          folder_names))
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/成功关注（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in kepro:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测协议号/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in fenjin:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    gzpd.drop({})
                    folder_to_clear = './检测协议号'
                    clear_folder(folder_to_clear)
                    
                elif sign == 'caijipd':
                    mingzi = text.split(':')
                    
                    link = mingzi[0]
                    days = int(mingzi[1])
                    
                    
                    gzpd_list = list(cji.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    yhm_list = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    
                    await context.bot.send_message(chat_id=user_id, text='开始采集，请稍等')
                    await asyncio.gather(
                        *(xycaijipd('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, link, days, yhm_list) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)
                    yhm_list1 = set(yhm_list)
                    yhm_list = list(yhm_list1)
                    with open('采集日志.txt', 'w', encoding='utf-8') as file:
                        for item in yhm_list:
                            file.write(item + '\n')
                    if yhm_list != []:
                        await context.bot.send_document(chat_id=user_id, document=open('采集日志.txt', "rb"))
                    cji.drop({})

                
                
                elif sign == 'xygjj':
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(xyxgjianjie('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, mingzi) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/成功修改（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./检测协议号/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测协议号/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./检测协议号/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    xgmz.drop({})
                    folder_to_clear = './检测协议号'
                    clear_folder(folder_to_clear)
                
                elif sign == 'zdgjj':
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(zdxgjianjie('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, mingzi) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/成功修改（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测号包/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    xgmz.drop({})
                    folder_to_clear = './检测号包'
                    clear_folder(folder_to_clear)
                    
                
                elif sign == 'xygname':

                    
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(xyxgmzi('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, mingzi) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/成功修改（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./检测协议号/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测协议号/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./检测协议号/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    xgmz.drop({})
                    folder_to_clear = './检测协议号'
                    clear_folder(folder_to_clear)
                    
                elif sign == 'zdgwzname':
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(zdxgmzi('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, mingzi) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/成功修改（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测号包/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    xgmz.drop({})
                    folder_to_clear = './检测号包'
                    clear_folder(folder_to_clear)
                
                elif sign == 'zdzpdjqr':
                    gzlb = text.split(' ')
                    
                    
                    gzpd_list = list(gzpd.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(zdgzpd('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, gzlb) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/成功关注（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测号包/死号（{len(fenjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    gzpd.drop({})
                    folder_to_clear = './检测号包'
                    clear_folder(folder_to_clear)
                    
                elif 'zdxyfen' in sign:
                    hbsl = int(sign.replace("zdxyfen ",''))
                    
                    fgsl = text.split(' ')
                    fgsum = 0
                    for i in fgsl:
                        fgsum += int(i)
                        
                    if fgsum > hbsl:
                        message_id = await context.bot.send_message(chat_id=user_id, text='指定的数量，超过号包数')
                        return
                    
                    await context.bot.send_message(chat_id=user_id, text='开始拆分')
                    
                    total_folders = context.user_data['xieyicaifen']
                    count = 0
                    for i in fgsl:
                        part_name = f"part_{i}.zip"

                        with zipfile.ZipFile(part_name, "w", zipfile.ZIP_DEFLATED) as part_zipf:
                            
                            # 将每个文件及其内容添加到 zip 文件中
                            for j in range(int(i)):
                                folder_name = total_folders[count]
                                count+=1
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", folder_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", folder_name + ".session")
                                if os.path.exists(json_file_path):
                                    part_zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    part_zipf.write(session_file_path, os.path.basename(session_file_path))
                        
                        
                        await context.bot.send_document(update.effective_chat.id, open(part_name, 'rb'))
                    
                elif 'zdcaifen' in sign:
                    hbsl = int(sign.replace("zdcaifen ",''))
                    
                    fgsl = text.split(' ')
                    fgsum = 0
                    for i in fgsl:
                        fgsum += int(i)
                        
                    if fgsum > hbsl:
                        message_id = await context.bot.send_message(chat_id=user_id, text='指定的数量，超过号包数')
                        return
                    
                    await context.bot.send_message(chat_id=user_id, text='开始拆分')
                    
                    total_folders = context.user_data['ysbcf']
                    count = 0
                    for i in fgsl:
                        part_name = f"part_{i}.zip"
                        
                        with zipfile.ZipFile(part_name, 'w') as part_zipf:
                            for j in range(int(i)):
                                folder_name = total_folders[count]
                                count+=1
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            part_zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                        
                        
                        
                        
                        await context.bot.send_document(update.effective_chat.id, open(part_name, 'rb'))
                        

                        
                        
                        
                    user.update_one({'user_id': user_id},{"$set":{'sign': 0}})
                elif 'xyxineb' in sign:
                    jeb = sign.replace('xyxineb ', '')
                    
                    gghlen = len(context.user_data[f'xygeb{user_id}'])

                    fstext = f'''
待更改号数: {gghlen}
旧二步: {jeb}
新二步: {text}
                    '''
                    user.update_one({'user_id': user_id}, {"$set": {'sign': 0}})

                    keyboard = [
                        [InlineKeyboardButton('确认修改', callback_data=f'qrxxygeb {jeb}:{text}')]
                    ]

                    await context.bot.send_message(chat_id=user_id, text=fstext,
                                                   reply_markup=InlineKeyboardMarkup(keyboard))
                elif 'xineb' in sign:
                    jeb = sign.replace('xineb ', '')
                    gghlen = len(context.user_data[f'zdgeb{user_id}'])
                    fstext = f'''
待更改号数: {gghlen}
旧二步: {jeb}
新二步: {text}
                    '''
                    user.update_one({'user_id': user_id}, {"$set": {'sign': 0}})

                    keyboard = [
                        [InlineKeyboardButton('确认修改', callback_data=f'qrxgeb {jeb}:{text}')]
                    ]

                    await context.bot.send_message(chat_id=user_id, text=fstext,
                                                   reply_markup=InlineKeyboardMarkup(keyboard))
                                                   
                elif 'dewbfen' in sign:
                    
                    
                    
                    await context.bot.send_message(chat_id=user_id, text='开始拆分')
                    split_count = int(text)
                    
                    total_folders = context.user_data['wbwjcf']

                    folders_per_part = len(total_folders) // split_count
                    
                    for i in range(split_count):
                        part_name = f"part_{i+1}.txt"
                        start_index = i * folders_per_part
                        end_index = (i + 1) * folders_per_part
                        with open(part_name, 'w+', encoding='utf-8') as part_zipf:
                            for j in range(start_index, end_index):
                                
                                folder_name = total_folders[j]
                                # full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                part_zipf.write(folder_name +'\n')
                        
                        
                        
                        await context.bot.send_document(update.effective_chat.id, open(part_name, 'rb'))
                    
                elif 'dexywbshu' in sign:
                    
                    await context.bot.send_message(chat_id=user_id, text='开始拆分')
                    split_count = int(text)
                    
                    total_folders = context.user_data['xieyicaifen']

                    folders_per_part = len(total_folders) // split_count
                    
                    for i in range(split_count):
                        part_name = f"part_{i+1}.zip"
                        start_index = i * folders_per_part
                        end_index = (i + 1) * folders_per_part
                        

                        with zipfile.ZipFile(part_name, "w", zipfile.ZIP_DEFLATED) as part_zipf:
                            
                            # 将每个文件及其内容添加到 zip 文件中
                            for j in range(start_index, end_index):
                                folder_name = total_folders[j]
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", folder_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", folder_name + ".session")
                                if os.path.exists(json_file_path):
                                    part_zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    part_zipf.write(session_file_path, os.path.basename(session_file_path))
                        
                        
                        await context.bot.send_document(update.effective_chat.id, open(part_name, 'rb'))
                        

                        
                        
                        
                    user.update_one({'user_id': user_id},{"$set":{'sign': 0}})
                
                elif 'dewbshu' in sign:
                    
                    await context.bot.send_message(chat_id=user_id, text='开始拆分')
                    split_count = int(text)
                    
                    total_folders = context.user_data['ysbcf']

                    folders_per_part = len(total_folders) // split_count
                    
                    for i in range(split_count):
                        part_name = f"part_{i+1}.zip"
                        start_index = i * folders_per_part
                        end_index = (i + 1) * folders_per_part
                        
                        with zipfile.ZipFile(part_name, 'w') as part_zipf:
                            for j in range(start_index, end_index):
                                folder_name = total_folders[j]
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            part_zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                        
                        
                        
                        
                        await context.bot.send_document(update.effective_chat.id, open(part_name, 'rb'))
                        

                        
                        
                        
                    user.update_one({'user_id': user_id},{"$set":{'sign': 0}})
                                
            elif update.message.document:
                if sign == 'plggeb':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./更改二步tdata/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    phone_dict = {}
                    phone_list = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    
                                    phone_dict[extracted_folder_name] = 1
                                    phone_list.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'更改二步tdata/')
                    
                    
                    context.user_data[f'zdgeb{user_id}'] = phone_list
                    
                    message_id = await context.bot.send_message(chat_id=user_id, text='发送旧二级，没有二级发无')

                    user.update_one({'user_id': user_id}, {"$set": {'sign': 'seteb'}})
                
                
                elif sign == 'xygedxb':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./更改二步tdata/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    phone_list = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    phone_list.append(fli1)
                                    
                                zip_ref.extract(member=file_info, path=f'更改二步tdata/')
                            else:
                                pass
                    context.user_data[f'xygeb{user_id}'] = phone_list
                            
                            
                    message_id = await context.bot.send_message(chat_id=user_id, text='发送旧二级，没有二级发无')

                    user.update_one({'user_id': user_id}, {"$set": {'sign': 'xyseteb'}})
                
                elif sign == 'zdgjj':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if xgmz.find_one({'phone': extracted_folder_name}) is None:
                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    session_files.append(extracted_folder_name)
                                    xgmz.insert_one({
                                        'projectname':'直登号',
                                        'uid': hbid,
                                        'phone': extracted_folder_name
                                    })
                            zip_ref.extract(file_info, f'检测号包/')
                    fstext = f'''
发送要修改的简介
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'zdgjj'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                
                
                
                elif sign == 'addjson':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    
                    # 定义压缩包和输出文件名
                    zip_file_path = new_file_path  # 替换为你的 zip 文件名
                    output_dir = 'output_jsons'  # 输出目录
                    
                    # 创建输出目录
                    os.makedirs(output_dir, exist_ok=True)
                    
                    # 解压 zip 文件
                    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                        zip_ref.extractall(output_dir)
                    
                    # 获取 cp.json 路径
                    cp_json_path = os.path.join('cp.json')
                    
                    # 遍历解压后的目录中的 .session 文件
                    for filename in os.listdir(output_dir):
                        if filename.endswith('.session'):
                            name_without_ext = os.path.splitext(filename)[0]
                            new_json_path = os.path.join(output_dir, f'{name_without_ext}.json')
                    
                            # 复制 cp.json 到新的 JSON 文件
                            shutil.copy(cp_json_path, new_json_path)
                    
                    # 将生成的 JSON 文件重新打包成 zip
                    with zipfile.ZipFile('output_jsons.zip', 'w', zipfile.ZIP_DEFLATED) as zip_out:
                        for filename in os.listdir(output_dir):
                            if filename.endswith('.json') or filename.endswith('.session'):
                                zip_out.write(os.path.join(output_dir, filename), filename)

                    await context.bot.send_document(chat_id=user_id, document=open('output_jsons.zip', "rb"))

                    folder_to_clear = 'output_jsons'
                    clear_folder(folder_to_clear)
                    
                elif sign == 'xyhfgj':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    hbid = generate_24bit_uid()
                                    session_files.append(fli1)
                                    jianceid.append(hbid)
                                        
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    await context.bot.send_message(chat_id=user_id, text='开始划分')
                    # 区号到文件名的映射
                    area_code_files = defaultdict(list)
                    
                    # 匹配区号的正则表达式
                    pattern = re.compile(r"(\+?\d{2})\d{8,}")
                    
                    for filename in session_files:
                        filename1 = filename
                        filename = filename.replace('+', '')
                        
                        if filename[0] == '1' or filename[0:2] == '+1':
                            area_code_files['+1'].append(filename)
                        else:
                            match = pattern.match(filename)
                            if match:
                                # 提取前两位
                                area_code = match.group(1)
                                area_code_files[area_code].append(filename1)
                    
                    # 打印结果
                    for area_code, files in area_code_files.items():
                        
                        zip_filename = f"sesstotdata/{area_code} {len(files)}个.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in files:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                        
                        time.sleep(3)
                    folder_to_clear = './sesstotdata'
                    clear_folder(folder_to_clear)
                    
                
                elif sign == 'xygjj':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测协议号/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    if xgmz.find_one({'phone': fli1}) is None:
                                        hbid = generate_24bit_uid()
                                        session_files.append(fli1)
                                        jianceid.append(hbid)
                                        xgmz.insert_one({
                                            'projectname':'协议号',
                                            'uid': hbid,
                                            'phone': fli1
                                        })
                                        
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                            
                            
                            
                    fstext = f'''
发送要修改的简介
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'xygjj'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                
                
                elif sign == 'xyfxlj':
                    
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./下载专用/{filename}'
                    await new_file.download(new_file_path)
                    link_list = []
                    with open(new_file_path, 'r', encoding='utf-8') as file:
                        # 逐行读取文件内容
                        for line in file:
                            # 去除每行末尾的换行符并添加到列表中
                            link_list.append(line.strip())
                    
                    link_list = []
                    with open(new_file_path, 'r', encoding='utf-8') as file:
                        # 逐行读取文件内容
                        for line in file:
                            # 去除每行末尾的换行符并添加到列表中
                            link_list.append(line.strip())
                    result = len(link_list) / 150
                    rounded_result = math.ceil(result)
                    
                    fstext = f'''
总共有{len(link_list)}个链接
需要发送{rounded_result}个协议号包
                    '''


                    context.user_data['xyfxlj'] = link_list
                    


                    user.update_one({'user_id': user_id}, {"$set": {"sign": f'xyf123xlj {rounded_result}'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)          
                    
                    

                            
                            
                            
#                     fstext = f'''
# 发送要分析的txt文件
#                     '''
                    
#                     user.update_one({'user_id': user_id}, {"$set": {"sign": 'xyf123xlj'}})
                    
                    
#                     message_id = await context.bot.send_message(chat_id=user_id,
#                                                                 text=fstext)
                
                elif 'xyf123xlj' in sign:
                    xyhbs = int(sign.replace('xyf123xlj ',''))
                    
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测协议号/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    session_files.append(fli1)
                                        
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                    if xyhbs != len(session_files):
                        fstext = f'''
应导入号包数: {xyhbs}
实际导入数: {session_files}
请重新导入
                        '''
                        message_id = await context.bot.send_message(chat_id=user_id,
                                                                                        text=fstext)
                        return
                    
                    fstext = f'''
开始分析
                    '''
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                                    text=fstext)
                    link_chunks = context.user_data['xyfxlj']
                    
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}

                    kylink = []
                    bklink = []
                    tasks = []
                    chunk_size = 150
                    link_chunks = [link_chunks[i:i + chunk_size] for i in range(0, len(link_chunks), chunk_size)]
                    for i, subfolder in enumerate(session_files):
                        if i < len(link_chunks):  # 确保不超出 link_chunks 的范围
                            link_chunk = link_chunks[i]
                            print(link_chunk)
                            
                            # await asyncio.gather(
                            #     *(xieyihaofenxi('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, link_list, kylink, bklink) for subfolder in
                            #       session_files))
                            task = xieyihaofenxi('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, link_chunk)
                            tasks.append(task)
                            
                    await asyncio.gather(*tasks)
                    
                    fstext = f'''
♻️ 检测数量：{len(session_files)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)
                    
                    shijiancuo = int(time.time())
                    
                    kylink = list(yhmfx.find({'state': 0}))
                    bklink = list(yhmfx.find({'state': 1}))
                    
                    if kylink != []:
                        
                        
                        kylink1 = []
                        for i in kylink:
                            
                            kylink1.append(i['yhm'])
                        
                        
                        kylink1 = '\n'.join(kylink1)
                        zip_filename = f"./下载专用/可用链接.txt"
                        with open(zip_filename, "w") as f:
                
                            f.write(kylink1)
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    if bklink != []:
                        bklink1 = []
                        for i in bklink:
                            bklink1.append(i['yhm'])
                        
                        
                        
                        bklink1 = '\n'.join(bklink1)
                        zip_filename = f"./下载专用/不可用链接.txt"
                        with open(zip_filename, "w") as f:
                
                            f.write(bklink1)
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    fxi.drop({})
                    yhmfx.drop({})
                    
                    
                elif sign == 'caijipd':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测协议号/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    if cji.find_one({'phone': fli1}) is None:
                                        hbid = generate_24bit_uid()
                                        session_files.append(fli1)
                                        jianceid.append(hbid)
                                        cji.insert_one({
                                            'projectname':'协议号',
                                            'uid': hbid,
                                            'phone': fli1
                                        })
                                        
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                            
                            
                            
                    fstext = f'''
发生要采集的频道或群组链接
不带@
比如 https://t.me/sihai
输 sihai:7
代表采集 sihai 采集7天内记录
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'caijipd'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                elif sign == 'xygname':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测协议号/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    if xgmz.find_one({'phone': fli1}) is None:
                                        hbid = generate_24bit_uid()
                                        session_files.append(fli1)
                                        jianceid.append(hbid)
                                        xgmz.insert_one({
                                            'projectname':'协议号',
                                            'uid': hbid,
                                            'phone': fli1
                                        })
                                        
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                            
                            
                            
                    fstext = f'''
发送要修改的名字
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'xygname'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                
                
                elif sign == 'zdgname':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if xgmz.find_one({'phone': extracted_folder_name}) is None:
                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    session_files.append(extracted_folder_name)
                                    xgmz.insert_one({
                                        'projectname':'直登号',
                                        'uid': hbid,
                                        'phone': extracted_folder_name
                                    })
                            zip_ref.extract(file_info, f'检测号包/')
                    fstext = f'''
发送要修改的名字
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'zdgwzname'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                elif sign == 'wbwjcf':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with open(new_file_path, 'r', encoding='utf-8') as file:
                        link_list = file.read()
                    link_list = link_list.split('\n')
                    context.user_data['wbwjcf'] = link_list        
                    fstext = f'''
共{len(link_list)}个
                    '''
                    keyboard = [
                        [InlineKeyboardButton('等额拆分', callback_data=f'dewbfen {filename}')]    
                    ]
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    
                    await context.bot.send_message(chat_id=user_id,text=fstext,reply_markup=InlineKeyboardMarkup(keyboard)) 
                
                
                elif sign == 'ggaiwezi':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    folder_names.append(fli1)
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    
                    context.user_data['ggaiwezi'] = folder_names        
                    fstext = f'''
共{len(folder_names)}个号

输入替换的二步
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'srthwenzi'}})
                    keyboard = [[InlineKeyboardButton('取消', callback_data=f'close {user_id}')]]
                    await context.bot.send_message(chat_id=user_id,text=fstext,reply_markup=InlineKeyboardMarkup(keyboard))
                  
                  
                  
                elif sign =='xieyicaifen':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in phone_dict.keys():
                                    phone_dict[fli1] = 1
                                    folder_names.append(fli1)
                                        
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                    context.user_data['xieyicaifen'] = folder_names        
                    fstext = f'''
共{len(folder_names)}个号
                    '''
                    keyboard = [
                        [InlineKeyboardButton('等额拆分', callback_data=f'dexyfen {filename}'), InlineKeyboardButton('指定拆分', callback_data=f'zdxyfen {len(folder_names)}')]    
                    ]
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    
                    await context.bot.send_message(chat_id=user_id,text=fstext,reply_markup=InlineKeyboardMarkup(keyboard))
                  
                elif sign == 'ysbcf':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'tdatatosession/')
                            
                    context.user_data['ysbcf'] = folder_names        
                    fstext = f'''
共{len(folder_names)}个号
                    '''
                    keyboard = [
                        [InlineKeyboardButton('等额拆分', callback_data=f'decaifen {filename}'), InlineKeyboardButton('指定拆分', callback_data=f'zdcaifen {len(folder_names)}')]    
                    ]
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    
                    await context.bot.send_message(chat_id=user_id,text=fstext,reply_markup=InlineKeyboardMarkup(keyboard))
                            
                    
                elif sign == 'downlink':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./下载专用/{filename}'
                    await new_file.download(new_file_path)

                    # 从文本文件中读取链接
                    with open(new_file_path, "r") as file:
                        content = file.read()

                    # 使用正则表达式提取链接
                    download_links = re.findall(r'(https?://\S+)', content)
                    message_id = await context.bot.send_message(chat_id=user_id, text='下载中，请稍后')

                    extracted_folders = []

                    phone_dict = {}

                    for i, download_link in enumerate(download_links, start=1):

                        # 发送 GET 请求获取压缩文件内容
                        try:
                            response = requests.get(download_link)

                            # 确保请求成功
                            if response.status_code == 200:
                                # 创建一个临时内存缓冲区
                                zip_buffer = io.BytesIO(response.content)

                                # 解压缩文件到当前目录、

                                with zipfile.ZipFile(zip_buffer, 'r') as zip_ref:
                                    for file_info in zip_ref.infolist():
                                        match = re.match(r'^([^/]+)/.*$', file_info.filename)
                                        if match:
                                            extracted_folder_name = match.group(1)

                                            if extracted_folder_name not in phone_dict.keys():
                                                phone_dict[extracted_folder_name] = 1
                                                extracted_folders.append(extracted_folder_name)
                                        zip_ref.extract(file_info, f'下载专用/')
                        except:
                            await context.bot.send_message(chat_id=user_id, text=f'{download_link}下载失败')
                        time.sleep(3)
                    shijiancuo = int(time.time())
                    zip_filename = f"./下载专用/{user_id}_{shijiancuo}.zip"
                    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                        # 将每个文件夹及其内容添加到 zip 文件中
                        for folder_name in extracted_folders:
                            full_folder_path = os.path.join(f"下载专用/", folder_name)
                            if os.path.exists(full_folder_path):
                                # 添加文件夹及其内容
                                for root, dirs, files in os.walk(full_folder_path):
                                    for file in files:
                                        file_path = os.path.join(root, file)
                                        # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                        zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                        full_folder_path)))
                            else:
                                # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                pass
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    folder_to_clear = './下载专用'
                    clear_folder(folder_to_clear)

            
                elif sign == 'xyjcsx':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    folder_names.append(fli1)
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    message_id = await context.bot.send_message(chat_id=user_id, text='协议号检测双向中，请稍后')
                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(xyshaungxiang('sesstotdata', subfolder, semaphore, result_dict, kepro, sxjin) for subfolder in folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}

正常: {result_dict['zc']}
双向: {result_dict['sx']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"sesstotdata/自由小鸟（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in kepro:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    if len(sxjin) != 0:
                        zip_filename = f"sesstotdata/双向（{len(sxjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in sxjin:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


                    
                    folder_to_clear = './sesstotdata'
                    clear_folder(folder_to_clear)


                elif sign == 'jcshuax':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'tdatatosession/')

                    message_id = await context.bot.send_message(chat_id=user_id, text='直登号检测双向中，请稍后')

                    kepro = []
                    fenjin = []
                    sxjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0}
                    await asyncio.gather(
                        *(zdshuangxiang('tdatatosession', subfolder, semaphore, result_dict, kepro, sxjin) for subfolder in
                          folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}

正常: {result_dict['zc']}
双向: {result_dict['sx']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)

 
                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"tdatatosession/自由小鸟（{len(kepro)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    if len(sxjin) != 0:
                        zip_filename = f"tdatatosession/双向（{len(sxjin)}）.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sxjin:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './tdatatosession'
                    clear_folder(folder_to_clear)


                elif sign == 'tdatatosession':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'tdatatosession/')

                    message_id = await context.bot.send_message(chat_id=user_id, text='tdata to session中，请稍后')

                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(zhidengzhuan('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in
                          folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                                        '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in kepro:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"tdatatosession/", file_name + ".json")
                                session_file_path = os.path.join(f"tdatatosession/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    zip_filename = f"tdatatosession/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    folder_to_clear = './tdatatosession'
                    clear_folder(folder_to_clear)

                elif sign == 'sessiontotdata':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    folder_names.append(fli1)
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    message_id = await context.bot.send_message(chat_id=user_id, text='session to tdata中，请稍后')
                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(xieyizhuanzhideng('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件夹及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                json_file_path = os.path.join(f"./sesstotdata/", folder_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", folder_name + ".session")
                                if os.path.exists(json_file_path):
                                    copy_file(json_file_path, f'./sesstotdata/{folder_name}/')
                                if os.path.exists(session_file_path):
                                    copy_file(session_file_path, f'./sesstotdata/{folder_name}/')
                                
                                full_folder_path = os.path.join(f"./sesstotdata/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                                
                                
                                
                                
     
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    
                    zip_filename = f"./sesstotdata/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in fenjin:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './sesstotdata'
                    clear_folder(folder_to_clear)



                elif sign == 'xyjcch':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    
                    ch_list = []
                    sh_list = []
                    dj_list = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    hbid = generate_24bit_uid()
                                    session_files.append(fli1)
                                    jianceid.append(hbid)
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass

                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    await context.bot.send_message(chat_id=user_id,
                                                                text='检测号存活中，超过10分钟没反应联系技术')


                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'dj': 0}
                    await asyncio.gather(
                        *(xieyijiance('检测协议号', subfolder, semaphore, result_dict,ch_list, sh_list, dj_list) for subfolder in session_files))


                    fstext = f'''
♻️ 检测数量：{len(session_files)}

✅ 存活数量：{result_dict['alive']}

❌ 冻结数量：{result_dict['dj']}
❌ 死号数量：{result_dict['dead']}
'''
                    await context.bot.send_message(chat_id=user_id,text=fstext)

                    
                    shijiancuo = int(time.time())
                    zip_filename = f"./检测协议号/健康（{len(ch_list)}）.zip"
                    if len(ch_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in ch_list:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    
                    zip_filename = f"./检测协议号/冻结（{len(dj_list)}）.zip"
                    if len(dj_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in dj_list:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    zip_filename = f"./检测协议号/封禁（{len(sh_list)}）.zip"
                    if len(sh_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in sh_list:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    
                elif sign == 'xyzpdjqr':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    if gzpd.find_one({'phone': fli1}) is None:
                                        hbid = generate_24bit_uid()
                                        session_files.append(fli1)
                                        jianceid.append(hbid)
                                        gzpd.insert_one({
                                            'projectname':'协议号',
                                            'uid': hbid,
                                            'phone': fli1
                                        })
                                zip_ref.extract(member=file_info, path=f'检测协议号/')
                            else:
                                pass
                    fstext = f'''
发送要关注的频道 和机器人用户名 用空格分隔
@Tdatasession9bot @topnine99999999
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'xyzpdjqr'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                elif sign == 'zdzpdjqr':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if gzpd.find_one({'phone': extracted_folder_name}) is None:
                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    session_files.append(extracted_folder_name)
                                    gzpd.insert_one({
                                        'projectname':'直登号',
                                        'uid': hbid,
                                        'phone': extracted_folder_name
                                    })
                            zip_ref.extract(file_info, f'检测号包/')
                    fstext = f'''
发送要关注的频道 和机器人用户名 用空格分隔
@Tdatasession9bot @topnine99999999
                    '''
                    
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 'zdzpdjqr'}})
                    
                    
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text=fstext)
                
                
                elif sign == 'xyzz2fa':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    folder_names.append(fli1)
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    message_id = await context.bot.send_message(chat_id=user_id, text='重置二步中，请稍后')
                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(xyerbzz('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in kepro:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                                

                    
                    zip_filename = f"./sesstotdata/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in fenjin:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './sesstotdata'
                    clear_folder(folder_to_clear)
                    
                elif sign == 'xytcqtsb':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./sesstotdata/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            filename = file_info.filename
                            if filename.endswith('.json') or filename.endswith('.session'):
                                # 仅解压 session 或者 json 格式的文件
                                fli1 = filename.replace('.json', '').replace('.session', '')
                                if fli1 not in tj_dict.keys():
                                    tj_dict[fli1] = 1

                                    folder_names.append(fli1)
                                zip_ref.extract(member=file_info, path=f'sesstotdata/')
                            else:
                                pass
                    message_id = await context.bot.send_message(chat_id=user_id, text='踢出设备中，请稍后')
                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(xytcsb('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in kepro:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                                

                    
                    zip_filename = f"./sesstotdata/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in fenjin:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './sesstotdata'
                    clear_folder(folder_to_clear)
                    
                    
                elif sign == 'tcqtsb':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'tdatatosession/')

                    message_id = await context.bot.send_message(chat_id=user_id, text='踢出设备中，请稍后')

                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(zdqtcbsb('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in
                          folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                                        '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    zip_filename = f"tdatatosession/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    folder_to_clear = './tdatatosession'
                    clear_folder(folder_to_clear)
                    
                elif sign == 'zdzz2fa':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./tdatatosession/{filename}'
                    await new_file.download(new_file_path)
                    tj_dict = {}
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'tdatatosession/')

                    message_id = await context.bot.send_message(chat_id=user_id, text='重置二步中，请稍后')

                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0}
                    await asyncio.gather(
                        *(zderbzz('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin) for subfolder in
                          folder_names))

                    fstext = f'''
♻️ 检测数量：{len(folder_names)}

✅ 存活数量：{result_dict['alive']}

❌ 死号数量：{result_dict['dead']}
                                        '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/健康（{len(kepro)}）.zip"
                    if len(kepro) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in kepro:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    zip_filename = f"tdatatosession/封禁（{len(fenjin)}）.zip"
                    if len(fenjin) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in fenjin:
                                full_folder_path = os.path.join(f"./tdatatosession/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    folder_to_clear = './tdatatosession'
                    clear_folder(folder_to_clear)
                    
                    
                elif sign == 'xadagd123':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    now_file_path = f'./检测号存活专用/已过滤.zip'
                    
                    
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        file_list = zip_ref.namelist()
                        new_files = [name.replace('-', '') for name in file_list]
                
                        with zipfile.ZipFile(now_file_path, 'w', zipfile.ZIP_DEFLATED) as new_zip:
                            for old_name, new_name in zip(file_list, new_files):
                                with zip_ref.open(old_name) as source:
                                    new_zip.writestr(new_name, source.read())
                    
                    await context.bot.send_document(chat_id=user_id, document=open(now_file_path, "rb"))
                elif sign == 'zdjcch':
                    caption = update.message.caption
                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./检测号存活专用/{filename}'
                    await new_file.download(new_file_path)
                    jianceid = []
                    tj_dict = {}
                    session_files = []
                    ch_list = []
                    sh_list = []
                    dj_list = []
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)
                                if extracted_folder_name not in tj_dict.keys():
                                    tj_dict[extracted_folder_name] = 1
                                    hbid = generate_24bit_uid()
                                    jianceid.append(hbid)
                                    session_files.append(extracted_folder_name)

                            zip_ref.extract(file_info, f'检测号包/')


                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    message_id = await context.bot.send_message(chat_id=user_id,
                                                                text='检测号存活中，超过10分钟没反应联系技术')

                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'dj': 0}
                    await asyncio.gather(
                        *(jiancecunhuo('检测号包', subfolder, semaphore, result_dict, ch_list, sh_list, dj_list) for subfolder in session_files))

                    fstext = f'''
♻️ 检测数量：{len(session_files)}

✅ 存活数量：{result_dict['alive']}

❌ 冻结数量：{result_dict['dj']}
❌ 死号数量：{result_dict['dead']}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    zip_filename = f"./检测号包/健康（{len(ch_list)}）.zip"
                    if len(ch_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件夹及其内容添加到 zip 文件中
                            for folder_name in ch_list:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                        
                    zip_filename = f"./检测号包/冻结（{len(dj_list)}）.zip"

                    if len(dj_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件夹及其内容添加到 zip 文件中
                            for folder_name in dj_list:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    zip_filename = f"./检测号包/封禁（{len(sh_list)}）.zip"
                    
                    if len(sh_list) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件夹及其内容添加到 zip 文件中
                            for folder_name in sh_list:
                                full_folder_path = os.path.join(f"./检测号包/", folder_name)
                                if os.path.exists(full_folder_path):
                                    # 添加文件夹及其内容
                                    for root, dirs, files in os.walk(full_folder_path):
                                        for file in files:
                                            file_path = os.path.join(root, file)
                                            # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                            zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                            full_folder_path)))
                                else:
                                    # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                    pass
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    
                elif sign == 'add2fa':

                    caption = update.message.caption

                    if caption is None:
                        keyboard = [[InlineKeyboardButton('取消检测', callback_data=f'close {user_id}')]]
                        await context.bot.send_message(chat_id=user_id, text='请附带二步验证',
                                                       reply_markup=InlineKeyboardMarkup(keyboard))
                        return

                    file = update.message.document
                    # 获取文件名
                    filename = file.file_name

                    # 获取文件ID
                    file_id = file.file_id
                    new_file = await context.bot.get_file(file_id)
                    # 将文件保存到本地
                    new_file_path = f'./添加二步专用/{filename}'
                    await new_file.download(new_file_path)

                    await context.bot.send_message(chat_id=user_id, text='处理中，请稍后')
                    folder_names = []
                    phone_dict = {}
                    with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                        for file_info in zip_ref.infolist():
                            match = re.match(r'^([^/]+)/.*$', file_info.filename)
                            if match:
                                extracted_folder_name = match.group(1)

                                if extracted_folder_name not in phone_dict.keys():
                                    phone_dict[extracted_folder_name] = 1
                                    folder_names.append(extracted_folder_name)
                            zip_ref.extract(file_info, f'添加二步号包/')

                    for i in folder_names:
                        with open(f'添加二步号包/{i}/2fa.txt', 'w') as f:
                            f.write(f'{caption}')

                    shijiancuo = int(time.time())
                    zip_filename = f"./已添加二步/{user_id}_{shijiancuo}.zip"
                    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                        # 将每个文件夹及其内容添加到 zip 文件中
                        for folder_name in folder_names:
                            full_folder_path = os.path.join(f"./添加二步号包/", folder_name)
                            if os.path.exists(full_folder_path):
                                # 添加文件夹及其内容
                                for root, dirs, files in os.walk(full_folder_path):
                                    for file in files:
                                        file_path = os.path.join(root, file)
                                        # 使用相对路径在压缩包中添加文件，并设置压缩包内部的路径
                                        zipf.write(file_path, os.path.join(folder_name, os.path.relpath(file_path,
                                                                                                        full_folder_path)))
                            else:
                                # update.message.reply_text(f"文件夹 '{folder _name}' 不存在！")
                                pass
                    user.update_one({'user_id': user_id}, {"$set": {"sign": 0}})
                    await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))


def init(token):
    application = Application.builder().concurrent_updates(3).token(token).build()
    application.add_handlers(handlers={
        -1: [

        ],
        1: [
            CommandHandler('start', start),

            MessageHandler(
                (filters.TEXT | filters.PHOTO | filters.ANIMATION | filters.VIDEO | filters.ALL) & ~(filters.COMMAND),
                textkeyboard),
            CallbackQueryHandler(close, pattern='close '),
            CallbackQueryHandler(jcehao, pattern='jcehao'),
            CallbackQueryHandler(add2fa, pattern='add2fa'),
            CallbackQueryHandler(tdatatosession, pattern='tdatatosession'),
            CallbackQueryHandler(sessiontotdata, pattern='sessiontotdata'),
            CallbackQueryHandler(downlink, pattern='downlink'),
            CallbackQueryHandler(plggeb, pattern='plggeb'),
            CallbackQueryHandler(xyjcch, pattern='xyjcch'),
            CallbackQueryHandler(zdjcch, pattern='zdjcch'),
            CallbackQueryHandler(qrxgeb, pattern='qrxgeb '),
            CallbackQueryHandler(jcshuax, pattern='jcshuax'),
            CallbackQueryHandler(xyjcsx , pattern='xyjcsx'),
            CallbackQueryHandler(ysbcf , pattern='ysbcf'),
            CallbackQueryHandler(wbwjcf , pattern='wbwjcf'),
            CallbackQueryHandler(decaifen , pattern='decaifen '),
            CallbackQueryHandler(zdcaifen , pattern='zdcaifen '),
            CallbackQueryHandler(dewbfen , pattern='dewbfen '),
            CallbackQueryHandler(zdzpdjqr , pattern='zdzpdjqr'),
            CallbackQueryHandler(xyzpdjqr , pattern='xyzpdjqr'),
            CallbackQueryHandler(zdzz2fa , pattern='zdzz2fa'),
            CallbackQueryHandler(xyzz2fa , pattern='xyzz2fa'),
            CallbackQueryHandler(tcqtsb , pattern='tcqtsb'),
            CallbackQueryHandler(ggaiwezi , pattern='ggaiwezi'),
            CallbackQueryHandler(zdgname , pattern='zdgname'),
            CallbackQueryHandler(xygname , pattern='xygname'),
            CallbackQueryHandler(zdgjj , pattern='zdgjj'),
            CallbackQueryHandler(xygjj , pattern='xygjj'),
            CallbackQueryHandler(caijipd , pattern='caijipd'),
            CallbackQueryHandler(xyfxlj , pattern='xyfxlj'),
            CallbackQueryHandler(xyhfgj , pattern='xyhfgj'),
            CallbackQueryHandler(xytcqtsb , pattern='xytcqtsb'),
            CallbackQueryHandler(xygedxb , pattern='xygedxb'),
            CallbackQueryHandler(qrxxygeb , pattern='qrxxygeb '),
            CallbackQueryHandler(xadagd123 , pattern='xadagd123'),
            CallbackQueryHandler(addjson , pattern='addjson'),
            CallbackQueryHandler(xieyicaifen , pattern='xieyicaifen'),
            CallbackQueryHandler(dexyfen , pattern='dexyfen '),
            CallbackQueryHandler(zdxyfen , pattern='zdxyfen '),
        ]
    })
    # application.job_queue.run_repeating(callback=fasongmessage, interval=3)
    application.run_polling()


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))
    for i in ['检测协议号', '检测号包', '临时session', '检测号存活专用', 'tdatatosession', '已添加二步', '添加二步号包',
              '添加二步专用', 'sesstotdata', '下载专用','更改二步tdata', '二步号包']:
        create_folder_if_not_exists(i)
    init('7352528099:AAFPiuUMYx2CjKzMWf7PsqlX41yVerbknag')

