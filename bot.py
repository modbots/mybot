import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random
import json
from servergen import genserver
from subprocess import Popen

TOKEN = '5792941350:AAH-4wZamDd5UCseeJh5xDjiafKDs8SY2ao'
CHANNEL_ID = '@binbeginner'
NOT_SUB = 'Subscribe to this channel first'
ANOTHER_NOT_SUB = 'Subscription not found'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#return True if user is subscribed
def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.message_handler(commands=['server'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋 please choose any server you want to create GCP SSH account.We restricted one user one account policy to advoid SSH account polution.', reply_markup=nav.ServerMenu)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.message_handler(commands=['provider'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Hi there👋 please choose any server you want to create GCP SSH account.We restricted one user one account policy to advoid SSH account polution.', reply_markup=nav.ServerMenu)
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        #if user will try to write 'Profile' without subscription
        if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            if message.text == 'SERVERS':
                await bot.send_message(message.from_user.id, 'Hi there👋 please choose any server you want to create GCP SSH account.We restricted one user one account policy to advoid SSH account polution.', reply_markup=nav.ServerMenu)
            else:
                #await bot.send_message(message.from_user.id, 'Unknown command')
                pass
        else:
            await message.reply(NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.callback_query_handler(text='subdone')
async def subdone(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Hi there👋', reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)

@dp.callback_query_handler(text='inserver')#change this
async def inserver(message: types.Message):

    await bot.delete_message(message.from_user.id, message.message.message_id)
    
    no = random.randint(0,99)
    USERNAME = str(message.from_user.id)
    PASSWORD = message.from_user.first_name + str(no) + '@Sktool'
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        provider = []
        f = open('servers.json')
        data = json.load(f)
        for i in data['servers']:
            if i['serverName'] == "IN": # change this 
                provider.append(i)
        if not provider == []:
            randomerver = random.choice(provider)   
            SERVER_ID = randomerver['serverId']
            APP_ID = randomerver['appId']
            API_KEY = randomerver['apiKey']
            EMAIL= randomerver['email']
            DESCRIP = randomerver['description']
            IPADD = randomerver['serverIp']
            create = genserver(int(SERVER_ID),int(APP_ID),API_KEY,EMAIL,USERNAME,PASSWORD,DESCRIP,IPADD)
            await bot.send_message(message.from_user.id, f'Hi there👋 {create}')
        else:
            await bot.send_message(message.from_user.id, "Hi there👋 Currently we don't have any provider yet.")
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)



@dp.callback_query_handler(text='usserver')#change this
async def inserver(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    
    no = random.randint(0,99)
    USERNAME = str(message.from_user.id)
    PASSWORD = message.from_user.first_name + str(no) + '@Sktool'
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        provider = []
        f = open('servers.json')
        data = json.load(f)
        for i in data['servers']:
            if i['serverName'] == "US": # change this 
                provider.append(i)
        if not provider == []:
            randomerver = random.choice(provider)   
            SERVER_ID = randomerver['serverId']
            APP_ID = randomerver['appId']
            API_KEY = randomerver['apiKey']
            EMAIL= randomerver['email']
            DESCRIP = randomerver['description']
            IPADD = randomerver['serverIp']
            create = genserver(int(SERVER_ID),int(APP_ID),API_KEY,EMAIL,USERNAME,PASSWORD,DESCRIP,IPADD)
            await bot.send_message(message.from_user.id, f'Hi there👋 {create}')
        else:
            await bot.send_message(message.from_user.id, "Hi there👋 Currently we don't have any provider yet.")
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)



@dp.callback_query_handler(text='jpserver')#change this
async def inserver(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
   
    no = random.randint(0,99)
    USERNAME = str(message.from_user.id)
    PASSWORD = message.from_user.first_name + str(no) + '@Sktool'
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        provider = []
        f = open('servers.json')
        data = json.load(f)
        for i in data['servers']:
            if i['serverName'] == "JP": # change this 
                provider.append(i)
        if not provider == []:
            randomerver = random.choice(provider)   
            SERVER_ID = randomerver['serverId']
            APP_ID = randomerver['appId']
            API_KEY = randomerver['apiKey']
            EMAIL= randomerver['email']
            DESCRIP = randomerver['description']
            IPADD = randomerver['serverIp']
            create = genserver(int(SERVER_ID),int(APP_ID),API_KEY,EMAIL,USERNAME,PASSWORD,DESCRIP,IPADD)
            await bot.send_message(message.from_user.id, f'Hi there👋 {create}')
        else:
            await bot.send_message(message.from_user.id, "Hi there👋 Currently we don't have any provider yet.")
    else:
        await bot.send_message(message.from_user.id, ANOTHER_NOT_SUB, reply_markup=nav.checkSubMenu)


Popen(f"gunicorn server.server:app --bind 0.0.0.0:8080", shell=True)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
