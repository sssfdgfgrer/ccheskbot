from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters, Application, \
    ConversationHandler, ChatMemberHandler
from Crypto.Cipher import DES3
from mongo import *
import base64, random
from telethon import utils
import telethon, pickle, asyncio, os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
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

import asyncio, re, os, json, requests, io, subprocess
from pygtrans import Translate
from collections import defaultdict


hf_json = {
    'addjson': '发送一个协议号包',
    'ggaiwezi': '发送协议号包',
    'xadagd123': '发送一个号包',
    'xytcqtsb': f'''
🔥批量Session踢出设备
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
''',
    'tcqtsb': f'''
🔥批量Tdata踢出设备
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
''',
    'plggeb': f'''
🔥批量修改Tdata二级密码
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
''',
    'xygedxb': f'''
🔥批量修改Session二级密码
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'xyhfgj': '发送一个协议号包',
    'add2fa': '发送号包, 并附带二步验证',
    'caijipd': '发送一个协议号包',
    'xyfxlj': '发送txt文本',
    'zdgname': f'''
🔥批量修改账户名字
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号''',    
    
    'xygname': f'''
🔥批量修改账户名字
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号''',
    
    
    'zdgjj': f'''
🔥批量修改简介
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号''',
    'xygjj': f'''
🔥批量修改简介
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'zdzz2fa': f'''
🔥批量Tdata重置二步
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
''',
    'xyzz2fa': f'''
🔥批量Session重置二步
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
''',
    'zdzpdjqr': f'''
🔥可批量关注指定频道 每次只能发送一个频道
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'xyzpdjqr': f'''
🔥可批量关注指定频道 每次只能发送一个频道
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'ysbcf': '发送压缩包',
    'wbwjcf': '发送txt文本',
    'jcshuax': f'''
🔥檢查Tdata双向情況
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号''',
    'xyjcsx': f'''
🔥檢查Ssession双向情況
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号''',
    'zdjcch': f'''
🔥檢查Tdata存活情況
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'xyjcch': f'''
🔥檢查协议号存活情況
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
    ''',
    'tdatatosession': f'''
🔥 使用Tdata文件生成 session
🗂 请发送压缩包zip格式
‼️ 请不要发送超过10000个账号
    ''',
    'sessiontotdata': f'''
🔥 使用session文件生成 Tdata
🗂 请发送压缩包zip格式
‼️ 请不要发送超过10000个账号
    '''
}

keyboard_dict = {
    '添加json': 'addjson',
    '更改文字': 'ggaiwezi',
    '过滤-': 'xadagd123',
    'Tdata踢出其他设备': 'tcqtsb',
    'Session踢出其他设备': 'xytcqtsb',
    'Tdata修改二级密码': 'plggeb',
    'Session修改二级密码': 'xygedxb',
    '协议划分国家': 'xyhfgj',
    '添加二步验证文本': 'add2fa',
    '协议采集频道': 'caijipd',
    '协议分析链接': 'xyfxlj',
    'Tdata（直登）修改姓名': 'zdgname',
    'Session（协议）修改姓名': 'xygname',
    'Tdata（直登）修改简介': 'zdgjj',
    'Session（协议）修改简介': 'xygjj',
    'Tdata重置2FA': 'zdzz2fa',
    'Session重置2FA': 'xyzz2fa',
    'Tdata（直登）关注频道': 'zdzpdjqr',
    'Session（协议）关注频道': 'xyzpdjqr',
    '压缩包拆分': 'ysbcf',
    '文本文件拆分': 'wbwjcf',
    '检查Tdata双向': 'jcshuax',
    '检查Session双向': 'xyjcsx',
    '检查Tdata（直登）': 'zdjcch',
    '检查Session（协议）': 'xyjcch',
    'Tdata 转换session': 'tdatatosession',
    'Session 转换Tdata': 'sessiontotdata'
}


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

async def xygzpd(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
                result_dict['sb'] += 1
                await client.disconnect()
                sblist.append(phone)
                return
        
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
        
        
        
async def xyxgjianjie(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
            result_dict['sb'] += 1
            await client.disconnect()
            sblist.append(phone)
            return
        
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
    
        
async def zdxgjianjie(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
            result_dict['sb'] += 1
            await client.disconnect()
            sblist.append(phone)
            return
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def xyxgmzi(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
            result_dict['sb'] += 1
            await client.disconnect()
            sblist.append(phone)
            return
        
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
        
        
async def zdxgmzi(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
            result_dict['sb'] += 1
            await client.disconnect()
            sblist.append(phone)
            return
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()

async def zdgzpd(selected_item, phone, semaphore, result_dict, kepro, fenjin, gzlb, sblist):
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
                result_dict['sb'] += 1
                await client.disconnect()
                sblist.append(phone)
                return
        result_dict['alive'] += 1
        kepro.append(phone)
        await client.disconnect()
        
        
async def xieyizhuanzhideng(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            wxylist.append(phone)
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

async def xyerbzz(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            wxylist.append(phone)
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

async def xytcsb(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        file_path = f"{selected_item}/{phone}"
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            wxylist.append(phone)
            await client.disconnect()
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
        
        
        
        
async def zdqtcbsb(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"临时session/{phone}", flag=UseCurrentSession)

        file_path = f"临时session/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            wxylist.append(phone)
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
            
            
async def zderbzz(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"临时session/{phone}", flag=UseCurrentSession)

        file_path = f"临时session/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            wxylist.append(phone)
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
            
            
async def zhidengzhuan(selected_item, phone, semaphore, result_dict, kepro, fenjin, wxylist):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"tdatatosession/{phone}", flag=UseCurrentSession)

        file_path = f"tdatatosession/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            wxylist.append(phone)
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

async def plgaxyierbu(selected_item, phone, semaphore, result_dict, jeb, xeb, kepro, sbpro, fenjin):
    async with semaphore:
        jeb1 = jeb.split(' ')
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


        result_dict['alive'] += 1
        if jeb == '无':
            try:
                erbu = await client.edit_2fa(new_password=xeb)
                result_dict['cgeb'] += 1
                kepro.append(phone)
            except:
                result_dict['sbeb'] += 1
                sbpro.append(phone)
        else:
            ggstate = 0
            for eb in jeb1:
                try:
                    erbu = await client.edit_2fa(current_password=eb, new_password=xeb)
                    result_dict['cgeb'] += 1
                    kepro.append(phone)
                    ggstate = 1
                    break
                except Exception as f:
                    continue
            if ggstate == 0:
                result_dict['sbeb'] += 1
                sbpro.append(phone)
        await client.disconnect()



async def plgaierbu(selected_item, phone, semaphore, result_dict, jeb, xeb, kepro, sbpro, fenjin):
    async with semaphore:
        jeb1 = jeb.split(' ')
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"临时session/{phone}", flag=UseCurrentSession)

        file_path = f"临时session/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['dead'] += 1
            fenjin.append(phone)
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            fenjin.append(phone)
            await client.disconnect()
            if os.path.exists(file_path):
                os.remove(file_path)
            return

        # a = await client.get_me()
        # if a is None:
        #     result_dict['dead'] += 1
        #     await client.disconnect()
        #     if os.path.exists(file_path):
        #         os.remove(file_path)
        #     return
        result_dict['alive'] += 1
        if jeb == '无':
            try:
                erbu = await client.edit_2fa(new_password=xeb)
                result_dict['cgeb'] += 1
                kepro.append(phone)
            except:
                result_dict['sbeb'] += 1
                sbpro.append(phone)
        else:
            ggstate = 0
            for eb in jeb1:
                try:
                    erbu = await client.edit_2fa(current_password=eb, new_password=xeb)
                    result_dict['cgeb'] += 1
                    kepro.append(phone)
                    ggstate = 1
                    break
                except Exception as f:
                    continue
            if ggstate == 0:
                result_dict['sbeb'] += 1
                sbpro.append(phone)
        await client.disconnect()
        if os.path.exists(file_path):
            os.remove(file_path)


async def zdshuangxiang(selected_item, phone, semaphore, result_dict, kepro, sxjin, wxylist, bkylist):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        
        assert tdesk.isLoaded()
        client = await tdesk.ToTelethon(session=f"{selected_item}/{phone}", flag=UseCurrentSession)

        file_path = f"{selected_item}/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            wxylist.append(phone)
            await client.disconnect()
            return

        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            bkylist.append(phone)
            await client.disconnect()
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            bkylist.append(phone)
            await client.disconnect()
            return
        result_dict['alive'] += 1
        
        
        try:
            await client.send_message('SpamBot', '/start')
            await asyncio.sleep(0.5)
            entity = await client.get_entity(178220800)
        except:
            result_dict['dead'] += 1
            bkylist.append(phone)
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
        if os.path.exists(file_path):
            os.remove(file_path)


async def xyshaungxiang(selected_item, phone, semaphore, result_dict, kepro, sxjin, wxylist, kylist, bkylist):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            wxylist.append(phone)
            await client.disconnect()
            return

        except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
            result_dict['dead'] += 1
            bkylist.append(phone)
            await client.disconnect()
            return
        a = await client.get_me()
        if a is None:
            result_dict['dead'] += 1
            bkylist.append(phone)
            await client.disconnect()
            return
        result_dict['alive'] += 1
        
        
        
        try:
            await client.send_message('SpamBot', '/start')
            await asyncio.sleep(0.5)
            entity = await client.get_entity(178220800)
        except:
            result_dict['dead'] += 1
            bkylist.append(phone)
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
        
    

async def jiancecunhuo(selected_item, phone, semaphore, result_dict, ch_list, sh_list, wxylist):
    async with semaphore:
        lujin = f'{selected_item}/{phone}/tdata'
        tdesk = TDesktop(lujin)
        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=f"{selected_item}/{phone}", flag=UseCurrentSession)

        file_path = f"{selected_item}/{phone}.session"

        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            wxylist.append(phone)
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
        result_dict['alive'] += 1
        ch_list.append(phone)
        await client.disconnect()
        if os.path.exists(file_path):
            os.remove(file_path)



async def xieyijiance(selected_item, phone, semaphore, result_dict,ch_list, sh_list, wxylist):
    async with semaphore:
        oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id=f"{phone}")
        client = TelegramClient(f"{selected_item}/{phone}",oldAPI,timeout=20)
        try:
            await asyncio.wait_for(client.connect(), 20)
        except asyncio.exceptions.TimeoutError:
            result_dict['wxy'] += 1
            await client.disconnect()
            wxylist.append(phone)
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
    for i in ['GTQG18','FUSUFH','moli010203','a8ppp','o7eth','o9eth','dluboqu', 'Tdatatosession', 'H_ugeojbk518', 'Darling8_888']:
        if username == i:
            user.update_one({'username': i}, {'$set': {'state': '4'}})
    # user_list = user.find_one({"user_id": user_id})
    # state = user_list['state']
    # if state != '4':
    #     return
    user_list = user.find_one({'user_id': user_id})
    ptgrade = user_list['ptgrade']
    if ptgrade == '新用户':
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        now = datetime.now()
        Expiration = (now + timedelta(hours=6)).strftime(f"%Y-%m-%d %H:{timer[-5:]}")
        user.update_one({'user_id': user_id}, {"$set": {"Expiration": Expiration}})
        user.update_one({'user_id': user_id}, {"$set": {"ptgrade": '一般用户'}})
        await context.bot.send_message(chat_id=user_id,text=f'<b>机器人试用权截止: {Expiration}</b>', parse_mode='HTML')
    else:
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        Expiration = user_list['Expiration']
        if timer >= Expiration:
            await context.bot.send_message(chat_id=user_id,text=f'<b>已到期,联系管理员开卡</b>', parse_mode='HTML')
            return
        await context.bot.send_message(chat_id=user_id,text=f'<b>机器人试用权截止: {Expiration}</b>', parse_mode='HTML')
        
    keyboard = [
        [KeyboardButton("Tdata重置2FA"), KeyboardButton("Session重置2FA")],
        [KeyboardButton('Tdata踢出其他设备'), KeyboardButton('Session踢出其他设备')],
        [KeyboardButton('Tdata修改二级密码'), KeyboardButton('Session修改二级密码')],
        [KeyboardButton('Tdata（直登）修改姓名'), KeyboardButton('Session（协议）修改姓名')],
        [KeyboardButton('Tdata（直登）修改简介'), KeyboardButton('Session（协议）修改简介')],
        [KeyboardButton('Tdata（直登）关注频道'), KeyboardButton('Session（协议）关注频道')],
        [KeyboardButton('检查Tdata双向'), KeyboardButton('检查Session双向')],
        [KeyboardButton('检查Tdata（直登）'), KeyboardButton('检查Session（协议）')],
        [KeyboardButton('Tdata 转换session'), KeyboardButton('Session 转换Tdata')]
    ] 
    # keyboard = [
    #     [KeyboardButton('添加json')],
    #     [KeyboardButton('更改文字'), KeyboardButton('过滤-')],
    #     [KeyboardButton('Tdata踢出其他设备'), KeyboardButton('Session踢出其他设备')],
    #     [KeyboardButton('Tdata修改二级密码'), KeyboardButton('Session修改二级密码')],
    #     [KeyboardButton('协议划分国家'), KeyboardButton('添加二步验证文本')],
    #     [KeyboardButton('协议采集频道'), KeyboardButton('协议分析链接')],
    #     [KeyboardButton('Tdata（直登）修改姓名'), KeyboardButton('Session（协议）修改姓名')],
    #     [KeyboardButton('Tdata（直登）修改简介'), KeyboardButton('Session（协议）修改简介')],
    #     [KeyboardButton('Tdata重置2FA'), KeyboardButton('Session重置2FA')],
    #     [KeyboardButton('Tdata（直登）关注频道'), KeyboardButton('Session（协议）关注频道')],
    #     [KeyboardButton('压缩包拆分'), KeyboardButton('文本文件拆分')],
    #     [KeyboardButton('检查Tdata双向'), KeyboardButton('检查Session双向')],
    #     [KeyboardButton('检查Tdata（直登）'), KeyboardButton('检查Session（协议）')],
    #     [KeyboardButton('Tdata 转换session'), KeyboardButton('Session 转换Tdata')]
    # ]
    fstext = f'''
<b>💥欢迎使用！
👇请查看底部按钮，并选择您需要的功能！</b>
    '''
    await context.bot.send_message(chat_id=user_id, text=fstext,reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True,
                                                                  one_time_keyboard=False),parse_mode='HTML')
    # keyboard = [
    #     [InlineKeyboardButton('添加json', callback_data='addjson')],
    #     [InlineKeyboardButton('更改文字', callback_data='ggaiwezi'), InlineKeyboardButton('过滤-', callback_data='xadagd123')],
    #     [InlineKeyboardButton('Tdata踢出其他设备', callback_data='tcqtsb'),InlineKeyboardButton('Session踢出其他设备', callback_data='xytcqtsb')],
    #     [InlineKeyboardButton('Tdata修改二级密码', callback_data='plggeb'), InlineKeyboardButton('Session修改二级密码', callback_data='xygedxb')],
    #     [InlineKeyboardButton('协议划分国家', callback_data='xyhfgj'),InlineKeyboardButton('添加二步验证文本', callback_data='add2fa')],
    #     [InlineKeyboardButton('协议采集频道', callback_data='caijipd'), InlineKeyboardButton('协议分析链接', callback_data='xyfxlj')],
    #     [InlineKeyboardButton('Tdata（直登）修改姓名', callback_data='zdgname'), InlineKeyboardButton("Session（协议）修改姓名", callback_data='xygname')],
    #     [InlineKeyboardButton('Tdata（直登）修改简介', callback_data='zdgjj'), InlineKeyboardButton("Session（协议）修改简介", callback_data='xygjj')],
    #     [InlineKeyboardButton('Tdata重置2FA', callback_data='zdzz2fa'), InlineKeyboardButton('Session重置2FA', callback_data='xyzz2fa')],
    #     [InlineKeyboardButton('Tdata（直登）关注频道', callback_data='zdzpdjqr'), InlineKeyboardButton('Session（协议）关注频道', callback_data='xyzpdjqr')],
    #     [InlineKeyboardButton('压缩包拆分', callback_data='ysbcf'), InlineKeyboardButton('文本文件拆分', callback_data='wbwjcf')],
    #     [InlineKeyboardButton('检查Tdata双向', callback_data='jcshuax'),InlineKeyboardButton('检查Session双向', callback_data='xyjcsx')],
    #     [InlineKeyboardButton("检查Tdata（直登）", callback_data='zdjcch'), InlineKeyboardButton('检查Session（协议）', callback_data='xyjcch')],
    #     [InlineKeyboardButton('Tdata 转换session', callback_data='tdatatosession'), InlineKeyboardButton('Session 转换Tdata', callback_data='sessiontotdata')]
    # ]
    # await context.bot.send_message(chat_id=user_id, text='后台', reply_markup=InlineKeyboardMarkup(keyboard))


async def addjson(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()
    bot_id = context.bot.id
    fstext = f'''
发送一个协议号包
    '''
    user.update_one({"user_id": user_id}, {"$set": {"sign": f'addjson'}})
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
    message_id = await context.bot.send_message(chat_id=user_id, text='<b>💫正在批量修改中，请等待···</b>', parse_mode='HTML')
    folder_names = []
    for i in gg_list:
        folder_names.append(i)
    kepro = []
    sbpro = []
    fenjin = []
    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
    result_dict = {'alive': 0, 'dead': 0, 'cgeb': 0, 'sbeb': 0, 'wxy': 0}
    await asyncio.gather(
        *(plgaxyierbu('更改二步tdata', subfolder, semaphore, result_dict, jeb,xeb, kepro, sbpro, fenjin) for subfolder in
          folder_names))

    fstext = f'''
<b>✅ 成功（修改成功）：{result_dict["cgeb"]}
⚠️ 錯誤（原二级密码错误）：{result_dict["sbeb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}</b>
            '''
    await context.bot.send_message(chat_id=user_id, text=fstext, parse_mode='HTML')

    folder_names = kepro
    xianswb = []
    
    
    if result_dict['cgeb'] != 0:
        shijiancuo = int(time.time())
        zip_filename = f"更改二步tdata/Session 修改成功2FA - {len(folder_names)}.zip"
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
        shijiancuo = int(time.time())
        zip_filename = f"更改二步tdata/Session 修改失败2FA - {len(sbpro)}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
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
    
    if result_dict['dead'] != 0:
        shijiancuo = int(time.time())
        zip_filename = f"更改二步tdata/Session 封禁死亡 - {len(sbpro)}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # 将每个文件及其内容添加到 zip 文件中
            for file_name in fenjin:
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
    gg_list = len(context.user_data[f'zdgeb{user_id}'])
    message_id = await context.bot.send_message(chat_id=user_id, text='<b>💫正在批量修改中，请等待···</b>', parse_mode='HTML')
    folder_names = []
    for i in gg_list:
        folder_names.append(i)
    kepro = []
    sbpro = []
    fenjin = []
    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
    result_dict = {'alive': 0, 'dead': 0, 'cgeb': 0, 'sbeb': 0, 'wxy': 0}
    await asyncio.gather(
        *(plgaierbu('更改二步tdata', subfolder, semaphore, result_dict, jeb,xeb, kepro, sbpro, fenjin) for subfolder in
          folder_names))

    fstext = f'''
<b>✅ 成功（修改成功）：{result_dict["cgeb"]}
⚠️ 錯誤（原二级密码错误）：{result_dict["sbeb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}</b>
            '''
    await context.bot.send_message(chat_id=user_id, text=fstext, parse_mode='HTML')

    folder_names = kepro
    xianswb = []

    for i in folder_names:
        with open(f'更改二步tdata/{i}/2fa.txt', 'w') as f:
            f.write(f'{xeb}')

    if result_dict['cgeb'] != 0:

        shijiancuo = int(time.time())
        zip_filename = f"./二步号包/Tdata修改成功2FA - {len(folder_names)}.zip"
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

        shijiancuo = int(time.time())
        zip_filename = f"./二步号包/Tdata修改失败2FA - {len(sbpro)}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
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
        
        
    if result_dict['dead'] != 0:

        shijiancuo = int(time.time())
        zip_filename = f"./二步号包/Tdata封禁死亡 - {len(fenjin)}.zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # 将每个文件夹及其内容添加到 zip 文件中
            for folder_name in fenjin:
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
🔥檢查Tdata存活情況
🗂请发送压缩包zip格式
⚠️请不要发送超过10000个账号
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


async def clqfclo(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = query.message.chat
    await query.answer()
    cxid = query.data.replace('clqfclo ', '')
    bot_id = context.bot.id
    chat_id = chat.id
    user_id = query.from_user.id
    fullname = query.from_user.full_name
    username = query.from_user.username
    timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    qfck.insert_one({
        'cxid': cxid,
        'user_id': user_id,
        'fullname': fullname,
        'username': username,
        'timer': timer
    })
    user.update_one({'user_id': user_id}, {'$set': {'sign': 0}})
    await context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)

async def qunfagg(context: CallbackContext):
    bot_id = context.bot.id
    qfid = context.job.data['qfid']
    fstext = context.job.data['fstext']
    cxid = context.job.data['cxid']
    user_id = context.job.data['user_id']

    for i in user.find({}):
        yh_id = i['user_id']
        keyboard = [[InlineKeyboardButton(' ✅已读', callback_data=f'clqfclo {cxid}')]]
        try:
            await context.bot.send_message(chat_id=i['user_id'], text=fstext, reply_markup=InlineKeyboardMarkup(keyboard))
        except:
            pass
        await asyncio.sleep(3)
    await context.bot.send_message(chat_id=user_id, text='广告发送完成')

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
        ptgrade = user_list['ptgrade']
        if ptgrade == '新用户':
            timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            now = datetime.now()
            Expiration = (now + timedelta(hours=6)).strftime(f"%Y-%m-%d %H:{timer[-5:]}")
            user.update_one({'user_id': user_id}, {"$set": {"Expiration": Expiration}})
            user.update_one({'user_id': user_id}, {"$set": {"ptgrade": '一般用户'}})
            await context.bot.send_message(chat_id=user_id,text=f'<b>机器人试用权截止: {Expiration}</b>', parse_mode='HTML')
        else:
            timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            Expiration = user_list['Expiration']
            if timer >= Expiration:
                await context.bot.send_message(chat_id=user_id,text=f'<b>已到期,联系管理员开卡</b>', parse_mode='HTML')
                return
        
        chinese_buttons = [
            '添加json',
            '更改文字',
            '过滤-',
            'Tdata踢出其他设备',
            'Session踢出其他设备',
            'Tdata修改二级密码',
            'Session修改二级密码',
            '协议划分国家',
            '添加二步验证文本',
            '协议采集频道',
            '协议分析链接',
            'Tdata（直登）修改姓名',
            'Session（协议）修改姓名',
            'Tdata（直登）修改简介',
            'Session（协议）修改简介',
            'Tdata重置2FA',
            'Session重置2FA',
            'Tdata（直登）关注频道',
            'Session（协议）关注频道',
            '压缩包拆分',
            '文本文件拆分',
            '检查Tdata双向',
            '检查Session双向',
            '检查Tdata（直登）',
            '检查Session（协议）',
            'Tdata 转换session',
            'Session 转换Tdata'
        ]

        if text in chinese_buttons:
            xgsign = keyboard_dict[text]
            
            fstext = hf_json[xgsign]
            fstext = fstext.replace(fstext, f'<b>{fstext}</b>')
            
            await context.bot.send_message(chat_id=user_id,text=fstext, parse_mode='HTML')
            user.update_one({'user_id': user_id},{"$set":{"sign": xgsign}})
        
            return
        if sign != 0:
            if update.message.text:

                if sign == 'seteb':
                    message_id = await context.bot.send_message(chat_id=user_id, text='👉请发送要修改的二级密码')
                    user.update_one({'user_id': user_id}, {"$set": {'sign': f'xineb {text}'}})
                
                elif sign == 'xyseteb':
                    message_id = await context.bot.send_message(chat_id=user_id, text='👉请发送要修改的二级密码')
                    user.update_one({'user_id': user_id}, {"$set": {'sign': f'xyxineb {text}'}})
                
                elif 'fbgg' in sign:
                    qfid = sign.replace('fbgg ', '')

                    fstext = context.user_data[f'{qfid}']

                    await context.bot.send_message(chat_id=user_id, text=f'开始发送广告, 查询ID为: <b>{text}</b>',
                                             parse_mode='HTML')

                    user.update_one({'user_id': user_id}, {"$set": {'sign': 0}})
                    context.job_queue.run_once(qunfagg, 1, data={'qfid': qfid, 'fstext': fstext, 'cxid': text,
                                                                    'user_id': user_id})
                    
                    
                    
                    
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
                    
                    
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                    
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    
                    await asyncio.gather(
                        *(xygzpd('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, gzlb, sblist) for subfolder in
                          folder_names))
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/Session成功关注 - {len(kepro)}.zip"
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
                      
                    if len(sblist) != 0:
                        zip_filename = f"检测协议号/Session修改失败 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in sblist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./检测协议号/", file_name + ".json")
                                session_file_path = os.path.join(f"./检测协议号/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
                    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                        
                    if len(fenjin) != 0:
                        zip_filename = f"检测协议号/Session封禁死亡 - {len(fenjin)}.zip"
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
                        
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                        
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    await asyncio.gather(
                        *(xyxgjianjie('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, mingzi, sblist) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/Session修改成功简介 - {len(kepro)}.zip"
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
                     
                     
                    if len(sblist) != 0:
                        zip_filename = f"检测协议号/Session修改失败简介 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sblist:
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
                        zip_filename = f"检测协议号/Session封禁死亡 - {len(fenjin)}.zip"
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
                    
                
                elif sign == 'zdgjj':
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                        
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    await asyncio.gather(
                        *(zdxgjianjie('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, mingzi, sblist) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/Tdata修改成功简介 - {len(kepro)}.zip"
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
                        
                    if len(sblist) != 0:
                        zip_filename = f"检测号包/Tdata修改失败简介 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sblist:
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
                        zip_filename = f"检测号包/Tdata封禁死亡 - {len(fenjin)}.zip"
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
                    
                    
                
                elif sign == 'xygname':

                    
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                        
                        
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    await asyncio.gather(
                        *(xyxgmzi('检测协议号', subfolder, semaphore, result_dict, kepro, fenjin, mingzi, sblist) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测协议号/Session修改成功名字 - {len(kepro)}.zip"
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
                        
                        
                    if len(sblist) != 0:
                        zip_filename = f"检测协议号/Session修改失败名字 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sblist:
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
                        zip_filename = f"检测协议号/Session封禁死亡 - {len(fenjin)}.zip"
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
                    
                    
                elif sign == 'zdgwzname':
                    mingzi = text
                    
                    
                    gzpd_list = list(xgmz.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                        
                        
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                        
                        
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    await asyncio.gather(
                        *(zdxgmzi('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, mingzi, sblist) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/Tdata修改成功名字 - {len(kepro)}.zip"
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
                        
                        
                    if len(sblist) != 0:
                        zip_filename = f"检测号包/Tdata修改失败 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sblist:
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
                        zip_filename = f"检测号包/Tdata封禁死亡 - {len(fenjin)}.zip"
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
                    
                
                elif sign == 'zdzpdjqr':
                    gzlb = text.split(' ')
                    
                    
                    gzpd_list = list(gzpd.find({}))
                    folder_names = []
                    for i in gzpd_list:
                        folder_names.append(i['phone'])
                        
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                        
                    kepro = []
                    fenjin = []
                    sxjin = []
                    sblist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'sb': 0}
                    await asyncio.gather(
                        *(zdgzpd('检测号包', subfolder, semaphore, result_dict, kepro, fenjin, gzlb, sblist) for subfolder in
                          folder_names))
                    
                    
                    fstext = f'''
✅ 成功（修改成功）：{result_dict["alive"]}
⚠️ 錯誤（修改失败）：{result_dict["sb"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext)


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"检测号包/Tdata成功关注 - {len(kepro)}.zip"
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
                        
                        
                    if len(sblist) != 0:
                        zip_filename = f"检测号包/Tdata修改失败 - {len(sblist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in sblist:
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
                        zip_filename = f"检测号包/Tdata封禁死亡 - {len(fenjin)}.zip"
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

                    message_id = await context.bot.send_message(chat_id=user_id, text='👇请发送当前的二级密码，如果没有，请发“无”')

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
                            
                    message_id = await context.bot.send_message(chat_id=user_id, text='👇请发送当前的二级密码，如果没有，请发“无”')

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
                    pattern = re.compile(r"(\+?\d+)(?=\d{10})")
                    
                    for filename in session_files:
                        match = pattern.match(filename)
                        if match:
                            area_code = match.group(1)
                            area_code_files[area_code].append(filename)
                    
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
请发送您要修改的名字（例如：TG号批发xx）
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
                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')
                    kepro = []
                    fenjin = []
                    sxjin = []
                    wxylist = []
                    kylist = []
                    bkylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(xyshaungxiang('sesstotdata', subfolder, semaphore, result_dict, kepro, sxjin, wxylist,kylist,bkylist) for subfolder in folder_names))

                    fstext = f'''
<b>✅ 成功（正常且无双向）：{result_dict["zc"]}
🫢 双向（双向限制）：{result_dict["sx"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
⚠️ 錯誤（服务器未响应）：{result_dict["wxy"]}</b>
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext, parse_mode='HTML')


                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"sesstotdata/session检测 -正常- {len(kepro)}.zip"
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
                        zip_filename = f"sesstotdata/session检测 -双向- {len(sxjin)}.zip"
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

                    if len(bkylist) != 0:
                        zip_filename = f"sesstotdata/session检测 -无效- {len(bkylist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in bkylist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    if len(wxylist) != 0:
                        zip_filename = f"sesstotdata/session检测 -错误- {len(wxylist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in wxylist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
    
    
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './sesstotdata'
                    


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

                    await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如无反应！请联系技术支持！</b>', parse_mode='HTML')

                    kepro = []
                    fenjin = []
                    sxjin = []
                    wxylist = []
                    bkylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'zc': 0, 'fk': 0, 'sx': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(zdshuangxiang('tdatatosession', subfolder, semaphore, result_dict, kepro, sxjin, wxylist, bkylist) for subfolder in
                          folder_names))

                    fstext = f'''
<b>✅ 成功（正常且无双向）：{result_dict["zc"]}
🫢  双向（双向限制）：{result_dict["sx"]}
❌ 無效（多ip，封禁）：{result_dict["dead"]}
⚠️ 錯誤（服务器未响应）：{result_dict["wxy"]}</b>
                    '''
                    await context.bot.send_message(chat_id=user_id, text=fstext, parse_mode='HTML')

 
                    shijiancuo = int(time.time())
                    if len(kepro) != 0:
                        zip_filename = f"tdatatosession/Tdata检测 -正常- {len(kepro)}.zip"
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
                        zip_filename = f"tdatatosession/Tdata检测 -双向- {len(sxjin)}.zip"
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
                    
                    if len(bkylist) != 0:
                        zip_filename = f"tdatatosession/Tdata检测 -无效- {len(bkylist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in bkylist:
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
                    
                    if len(wxylist) != 0:
                        zip_filename = f"tdatatosession/Tdata检测 -错误- {len(wxylist)}.zip"
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in wxylist:
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

                    message_id = await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持</b>', parse_mode='HTML')

                    kepro = []
                    wxylist = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(zhidengzhuan('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in
                          folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/Tdata转换session -存活- {len(kepro)}.zip"
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

                    zip_filename = f"tdatatosession/Tdata转换session -无效- {len(fenjin)}.zip"
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
                        
                    zip_filename = f"tdatatosession/Tdata转换session -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in wxylist:
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
                    message_id = await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持</b>', parse_mode='HTML')
                    kepro = []
                    fenjin = []
                    wxylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(xieyizhuanzhideng('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/session转换Tdata -存活- {len(kepro)}.zip"
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

                    
                    zip_filename = f"./sesstotdata/session转换Tdata -无效- {len(fenjin)}.zip"
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
                    
                    
                    zip_filename = f"./sesstotdata/session转换Tdata -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in wxylist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    folder_to_clear = './sesstotdata'
                    



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
                    wxylist = []
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
                    message_id = await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持</b>', parse_mode='HTML')


                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(xieyijiance('检测协议号', subfolder, semaphore, result_dict,ch_list, sh_list, wxylist) for subfolder in session_files))


                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')
                
                    
                    
                    shijiancuo = int(time.time())
                    zip_filename = f"./检测协议号/检查Session -存活- {len(ch_list)}.zip"
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
                    
                    
                    
                    
                    
                    zip_filename = f"./检测协议号/检查Session -无效- {len(sh_list)}.zip"
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
                        
                        
                    zip_filename = f"./检测协议号/检查Session -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in wxylist:
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
                    message_id = await context.bot.send_message(chat_id=user_id, text='🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持')
                    kepro = []
                    fenjin = []
                    wxylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(xyerbzz('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/协议重置二步 -成功- {len(kepro)}.zip"
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
                                

                    
                    zip_filename = f"./sesstotdata/协议重置二步 -无效- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in wxylist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))
                    
                    
                    zip_filename = f"./sesstotdata/协议重置二步 -错误- {len(fenjin)}.zip"
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
                    message_id = await context.bot.send_message(chat_id=user_id, text='🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持')
                    kepro = []
                    fenjin = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    wxylist = []
                    result_dict = {'alive': 0, 'dead': 0, 'wxy':0}
                    await asyncio.gather(
                        *(xytcsb('sesstotdata', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')



                    shijiancuo = int(time.time())
                    zip_filename = f"./sesstotdata/协议踢出设备 -成功- {len(kepro)}.zip"
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
                                


                    zip_filename = f"./sesstotdata/协议踢出设备 -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for file_name in wxylist:
                                # 检查是否存在以 .json 或 .session 结尾的文件
                                json_file_path = os.path.join(f"./sesstotdata/", file_name + ".json")
                                session_file_path = os.path.join(f"./sesstotdata/", file_name + ".session")
                                if os.path.exists(json_file_path):
                                    zipf.write(json_file_path, os.path.basename(json_file_path))
                                if os.path.exists(session_file_path):
                                    zipf.write(session_file_path, os.path.basename(session_file_path))
                        await context.bot.send_document(chat_id=user_id, document=open(zip_filename, "rb"))

                    
                    zip_filename = f"./sesstotdata/协议踢出设备 -无效- {len(fenjin)}.zip"
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

                    message_id = await context.bot.send_message(chat_id=user_id, text='🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持')

                    kepro = []
                    fenjin = []
                    wxylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(zdqtcbsb('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in
                          folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/直登踢出设备 -成功- {len(kepro)}.zip"
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


                    zip_filename = f"tdatatosession/直登踢出设备 -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in wxylist:
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

                    zip_filename = f"tdatatosession/直登踢出设备 -无效- {len(fenjin)}.zip"
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

                    message_id = await context.bot.send_message(chat_id=user_id, text='🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持')

                    kepro = []
                    fenjin = []
                    wxylist = []
                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0, 'wxy': 0}
                    await asyncio.gather(
                        *(zderbzz('tdatatosession', subfolder, semaphore, result_dict, kepro, fenjin, wxylist) for subfolder in
                          folder_names))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')

 
                    shijiancuo = int(time.time())
                    zip_filename = f"tdatatosession/直登重置二步 -成功- {len(kepro)}.zip"
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


                    zip_filename = f"tdatatosession/直登重置二步 -错误- {len(wxylist)}.zip"
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件及其内容添加到 zip 文件中
                            for folder_name in wxylist:
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



                    zip_filename = f"tdatatosession/直登重置二步 -无效- {len(fenjin)}.zip"
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
                    wxylist = []
                    
                    
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
                    message_id = await context.bot.send_message(chat_id=user_id, text='<b>🔄 正在处理中，请稍后！如超过5分钟无反应！请联系技术支持</b>', parse_mode='HTML')

                    semaphore = asyncio.Semaphore(10)  # Define semaphore with a limit of 5 concurrent tasks
                    result_dict = {'alive': 0, 'dead': 0,'wxy': 0}
                    await asyncio.gather(
                        *(jiancecunhuo('检测号包', subfolder, semaphore, result_dict, ch_list, sh_list, wxylist) for subfolder in session_files))

                    fstext = f'''
<b>✅ 成功（活跃数量）：{result_dict['alive']}
❌ 無效（多ip，封禁）：{result_dict['dead']}
⚠️ 錯誤（服务器未响应）：{result_dict['wxy']}</b>
'''
                    await context.bot.send_message(chat_id=user_id, text=fstext,parse_mode='HTML')


                    shijiancuo = int(time.time())
                    zip_filename = f"./检测号包/检查Tdata -存活- {len(ch_list)}.zip"
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
                    zip_filename = f"./检测号包/检查Tdata -无效- {len(sh_list)}.zip"
                    
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
                        
                        
                    zip_filename = f"./检测号包/检查Tdata -错误- {len(wxylist)}.zip"
                    
                    if len(wxylist) != 0:
                        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                            # 将每个文件夹及其内容添加到 zip 文件中
                            for folder_name in wxylist:
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


async def yhlist(update: Update, context: CallbackContext):
    chat = update.effective_chat
    # print(chat)
    if chat.type == 'private':
        user_id = chat['id']
        chat_id = user_id
        username = chat['username']
        firstname = chat['first_name']
        fullname = chat['full_name']
        
        
        jilu_list = list(user.find({}, limit=10, sort=[('creation_time', -1)]))
        keyboard = []
        text_list = []
        count = 1
        for i in jilu_list:
            df_id = i['user_id']
            df_username = i['username']
            df_fullname = i['fullname']
            USDT = i['USDT']
            text_list.append(
                f'{count}. <a href="tg://user?id={df_id}">{df_fullname}</a> ID:<code>{df_id}</code>-@{df_username}-余额:{USDT}')
            count += 1
        if len(list(user.find({}))) > 10:
            keyboard.append([InlineKeyboardButton('下一页', callback_data=f'yhnext 10:{count}')])

    
        text_list = '\n'.join(text_list)
        try:
            await context.bot.send_message(chat_id=user_id,text=text_list, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(keyboard))
        except:
            pass



async def yhnext(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    data = query.data.replace('yhnext ', '')
    page = data.split(":")[0]
    user_id = update.effective_user.id
    count = int(data.split(":")[1])
    keyboard = []
    text_list = []
    jilu_list = list(user.find({}, skip=int(page), limit=10, sort=[('creation_time', -1)]))
    for i in jilu_list:
        df_id = i['user_id']
        df_username = i['username']
        df_fullname = i['fullname'].replace("<","").replace('>','')
        USDT = i['USDT']
        text_list.append(
            f'{count}. <a href="tg://user?id={df_id}">{df_fullname}</a> ID:<code>{df_id}</code>-@{df_username}-余额:{USDT}')

        count += 1
    if len(list(user.find({}, skip=int(page)))) > 10:
        if int(page) == 0:
            keyboard.append([InlineKeyboardButton('下一页', callback_data=f'yhnext {int(page) + 10}:{count}')])
        else:
            keyboard.append([InlineKeyboardButton('上一页', callback_data=f'yhnext {int(page) - 10}:{count - 20}'),
                             InlineKeyboardButton('下一页', callback_data=f'yhnext {int(page) + 10}:{count}')])
    else:
        keyboard.append([InlineKeyboardButton('上一页', callback_data=f'yhnext {int(page) - 10}:{count - 20}')])

    text_list = '\n'.join(text_list)

    await query.edit_message_text(text=text_list, reply_markup=InlineKeyboardMarkup(keyboard),
                                parse_mode='HTML')


async def fbgg(update: Update, context: CallbackContext):
    chat = update.effective_chat
    # print(chat)
    if chat.type == 'private':
        user_id = chat['id']
        chat_id = user_id
        username = chat['username']
        firstname = chat['first_name']
        fullname = chat['full_name']
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        lastname = chat['last_name']
        text = update.message.text

        fstext = text.replace('/gg ', '')
        fstext1 = f'''
设置查询ID
        '''
        keyboard = [[InlineKeyboardButton('取消发送', callback_data=f'close {user_id}')]]

        qfid = generate_24bit_uid()

        context.user_data[f'{qfid}'] = fstext

        user.update_one({'user_id': user_id}, {"$set": {'sign': f'fbgg {qfid}'}})
        await context.bot.send_message(chat_id=user_id, text=fstext1, reply_markup=InlineKeyboardMarkup(keyboard))


async def getcha(update: Update, context: CallbackContext):
    chat = update.effective_chat
    if chat.type == 'private':
        user_id = chat['id']
        chat_id = user_id
        username = chat['username']
        firstname = chat['first_name']
        fullname = chat['full_name']
        timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        lastname = chat['last_name']
        text = update.message.text
        text1 = text.split(' ')
        user_list = user.find_one({'user_id': user_id})
        USDT = user_list['USDT']
        state = user_list['state']

        if len(text1) == 2:
            cxid = text1[1]

            jilu_list = list(qfck.find({'cxid': cxid}, limit=10, sort=[('timer', -1)]))
            keyboard = []
            text_list = []
            count = 1
            for i in jilu_list:
                df_id = i['user_id']
                df_username = i['username']
                df_fullname = i['fullname']
                timer = i['timer']
                text_list.append(
                    f'{count}. <a href="tg://user?id={df_id}">{df_fullname}</a> ID:<code>{df_id}</code>-@{df_username}-{timer}')
                count += 1
            if len(list(qfck.find({'cxid': cxid}))) > 10:
                keyboard.append([InlineKeyboardButton('下一页', callback_data=f'ckqfnext 10:{count}:{cxid}')])

            keyboard.append([InlineKeyboardButton('关闭', callback_data=f'close {user_id}')])

            text_list = '\n'.join(text_list)
            try:
                await context.bot.send_message(chat_id=user_id, text=text_list, parse_mode='HTML',
                                             reply_markup=InlineKeyboardMarkup(keyboard))
            except:
                pass

        else:
            await context.bot.send_message(chat_id=chat_id, text='格式为: /get 查询ID，有一个空格')


async def shengcheng(update: Update, context: CallbackContext):
    us = update.effective_user
    chat_id = update.effective_chat.id
    user_id = us.id
    username = us.username
    fullname = us.full_name
    lastname = us.last_name
    reply_to_message_id = update.effective_message.message_id
    user_list = user.find_one({'user_id': user_id})
    state = user_list['state']
    if state == '4':
        money = update.message.text.replace('生成', '')
        if is_number(money):
            money = int(money)
            t = time.time()
            shijiancuo = int(round(t * 1000000))
            jiamitext = f'{shijiancuo}黄色大鸭子{money}'
            jiami = encrypt('Lk5Uz3slx3BrAghS1aaW5AY1', jiamitext)
            CDK = f'CDK:{jiami}'
            keydata(shijiancuo, CDK, int(money))
            text = f'''
生成{money}天充值卡
<code>{CDK}</code>
            '''
            await context.bot.send_message(chat_id=user_id, text=text, parse_mode='HTML')
        else:
            await context.bot.send_message(chat_id=user_id, text='请输入数字生成, 例如生成111')


async def chongzhi(update: Update, context: CallbackContext):
    us = update.effective_user
    chat = update.effective_chat
    if chat['type'] == 'private':
        user_id = us.id
        fullname = us.full_name
        CDK = update.message.text.replace('CDK:', '').replace(' ', '')
        try:
            jiemitext = decrypt(CDK)
        except:
            text = f'''
充值CDK
充值失败请确认CDK
            '''
            await context.bot.send_message(chat_id=user_id, text=text, parse_mode='HTML')
            return
        if '黄色大鸭子' not in jiemitext:
            text = f'''
充值CDK
充值失败请确认CDK
            '''
            await context.bot.send_message(chat_id=user_id, text=text, parse_mode='HTML')
        retext = re.findall('\d+\.?\d*', jiemitext)
        shijiancuo = int(retext[0])
        money = int(float(retext[1]))
        czkmoney = int(float(retext[1]))
        if keytext.find_one({"bianhao": shijiancuo, 'user_id': {'$ne': None}}) == None:
            user_list = user.find_one({"user_id": user_id})
            ptgrade = user_list['ptgrade']
            if ptgrade == '新用户':
                await context.bot.send_message(chat_id=user_id,text='请先添加关键词后，在使用充值码')
            else:
                if money == 0:
                    keytext.update_one({"bianhao": shijiancuo}, {"$set": {"user_id": user_id}})
                    user.update_one({'user_id': user_id}, {"$set": {'Expiration': '9999-12-30 00:00:00'}})
                    text = f'''
充值永久卡
当前过期时间为: 9999-12-30 00:00:00
                    '''
                    await context.bot.send_message(chat_id=user_id, text=text)
                    return
                
                Expiration = user_list['Expiration']
                xianzaishijian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if xianzaishijian >= Expiration:
                    keytext.update_one({"bianhao": shijiancuo}, {"$set": {"user_id": user_id}})
                    Expiration = (datetime.now() + timedelta(days=+int(money))).strftime(f"%Y-%m-%d %H:%M:%S")
                    user.update_one({'user_id': user_id}, {"$set": {'Expiration': Expiration}})
                    text = f'''
使用{money}天充值卡
当前过期时间为: {Expiration}
    '''
                    await context.bot.send_message(chat_id=user_id, text=text)
                else:
                    to_now = datetime.strptime(Expiration, '%Y-%m-%d %H:%M:%S')
                    keytext.update_one({"bianhao": shijiancuo}, {"$set": {"user_id": user_id}})
                    Expiration = (to_now + timedelta(days=+int(money))).strftime(f"%Y-%m-%d %H:%M:%S")
                    user.update_one({'user_id': user_id}, {"$set": {'Expiration': Expiration}})
                    text = f'''
使用{money}天充值卡
当前过期时间为: {Expiration}
    '''
                    await context.bot.send_message(chat_id=user_id, text=text)
        else:
            text = f'''
充值CDK
CDK已使用,充值失败
            '''
            await context.bot.send_message(chat_id=user_id, text=text)


def encrypt(key, content):
    """
    DES3加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = key_bytes
    cipher = DES3.new(key_bytes, DES3.MODE_ECB)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result

def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用DES3加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = DES3.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if (bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text

def decrypt(text):
    cryptor = DES3.new(bytes('Lk5Uz3slx3BrAghS1aaW5AY1', encoding='utf-8'), DES3.MODE_ECB)
    b = str(cryptor.decrypt(base64.b64decode(text)), encoding='utf-8')
    return b

def init(token):
    application = Application.builder().concurrent_updates(3).token(token).build()
    application.add_handlers(handlers={
        -1: [

        ],
        1: [
            CommandHandler('start', start),
            CommandHandler('list', yhlist),
            CommandHandler('gg', fbgg),
            CommandHandler('get', getcha),
            
            
            MessageHandler(filters.Regex('生成\d+'), shengcheng),
            MessageHandler(filters.Regex('CDK'), chongzhi),
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
            CallbackQueryHandler(yhnext , pattern='yhnext '),
            CallbackQueryHandler(clqfclo , pattern='clqfclo '),
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
    init('7962591253:AAG01wk0JrpT_Q6nvKPA6EOuxzd2wb6T-CI')

