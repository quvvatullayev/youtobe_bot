from cgitb import text
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

TOKEN = '5699418530:AAF-rw_GFSO_DeL-19T4s2eiGDXLk6OSTIg'

class Youtube:
    def __init__(self) -> None:
        pass

    def start(self, update:Update, context:CallbackContext):
        id = int(update.message.from_user.id)
        text = 'Assalomu alaykum buzning botga hush kilibsiz!😀😃\nBizning botimz youtube dan vediyo, audio va suratlar yuklab olishingiz mimkun\nlinklarni tashlan📥'
        updater.bot.sendMessage(id, text)

    def get_vedio(self, update:Update, context:CallbackContext):
        text = update.message.text
        id = update.message.from_user.id
        print(text)
        # update.message.reply_photo(text)


updater = Updater(TOKEN)

youtube = Youtube()

# add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', youtube.start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, youtube.get_vedio))
#Start the bot
updater.start_polling()
updater.idle()