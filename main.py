from pytube import YouTube
from pytube import Playlist
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

    def get_audio(self, update:Update, context:CallbackContext):
        url = update.message.text
        id = update.message.from_user.id
        yt = YouTube(url)
        from io import BytesIO
        but = BytesIO()
        if yt.check_availability() is None:
            audio = yt.streams.get_audio_only()
            audio.stream_to_buffer(buffer=but)
            but.seek(0)
            title = yt.title
            updater.bot.sendAudio(id, but, caption=title)
        else:
            update.message.reply_text('Xatolik ...')

    def get_vidoe(self, update:Update, context:CallbackContext):
        pass

updater = Updater(TOKEN)

youtube = Youtube()

# add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', youtube.start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, youtube.get_audio))
#Start the bot
updater.start_polling()
updater.idle()