from tinydb import TinyDB 
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update
from tinydb.database import Document
import telegram
import json
import datetime

user = TinyDB("user.json")
txt = TinyDB('txt.json')
TOKEN = '5549407151:AAGVaQx5L2bvwBYnZE3a50yycdBQfPvl1fo'
updater = Updater(TOKEN)


def start(update:Updater, context:CallbackContext):
    user_id = update.message.chat.id
    bot = context.bot
    text = update.message.text 
    date = update.message.date
    txt.insert({"text":f'{text}', 'user_id':f"{user_id}", 'date':f'{date}'})

    arr = user.all()    
    list_1=[]
    for i in arr:
        list_1.append(i['user_id'])

    if str(user_id) not in list_1:
        user.insert({'user_id':f'{user_id}'})
    bot.sendMessage(user_id,'/start')

def main(update:Update, context:CallbackContext):
    text = update.message.text
    user_id = update.message.chat.id
    date = update.message.date
    tp = update.message.sticker
    txt.insert({"text":f'{text}','user_id':f"{user_id}", 'date':f'{date}'})


updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.all,main))

updater.start_polling()
updater.idle()