from pytube import YouTube
from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

TOKEN = '5699418530:AAF-rw_GFSO_DeL-19T4s2eiGDXLk6OSTIg'

class Youtube:
    def __init__(self) -> None:
        pass

    def start(self, update:Update, context:CallbackContext):
        id = int(update.message.from_user.id)
        text = 'Assalomu alaykum buzning botga hush kilibsiz!๐๐\nBizning botimz youtube dan vediyo, audio va suratlar yuklab olishingiz mimkun\nlinklarni tashlan๐ฅ'
        updater.bot.sendMessage(id, text)

    def text_sorch(self, update:Update, context:CallbackContext):
        query = update.callback_query
        id = update.message.from_user.id
        text = update.message.text
        inlineKeyboard = InlineKeyboardButton(f'๐นdp',callback_data=f'๐นdp{text}')
        inlineKeyboard1 = InlineKeyboardButton(f'๐MP3',callback_data=f'๐MP3{text}')
        inlineKeyboard3 = InlineKeyboardButton('๐ผ',callback_data=f'๐ผ{text}')
        reply_markup = InlineKeyboardMarkup([[inlineKeyboard,inlineKeyboard1], [inlineKeyboard3]])
        updater.bot.sendMessage(id, text, reply_markup=reply_markup)

    def get_audio(self, update:Update, context:CallbackContext):
        query = update.callback_query
        id = query.message.chat.id
        url = query.data[4:]
        query.edit_message_reply_markup(reply_markup=None)
        query.edit_message_text(text='๐ Audio havolasini yuboring YouTube!')
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
        query = update.callback_query
        id = query.message.chat.id
        url = query.data[3:]
        query.edit_message_reply_markup(reply_markup=None)
        query.edit_message_text(text='๐ Video havolasini yuboring YouTube!')
        yt = YouTube(url)
        from io import BytesIO
        but = BytesIO()
        if yt.check_availability() is None:
            audio = yt.streams.get_highest_resolution()
            audio.stream_to_buffer(buffer=but)
            but.seek(0)
            title = yt.title
            updater.bot.sendVideo(id, but, caption=title)
        else:
            update.message.reply_text('Xatolik ...')

    def get_img(self, update:Update, context:CallbackContext):
        query = update.callback_query
        id = query.message.chat.id
        url = query.data[1:]
        query.edit_message_reply_markup(reply_markup=None)
        query.edit_message_text(text='๐ Rasim havolasini yuboring YouTube!')
        yt = YouTube(url)
        from io import BytesIO
        but = BytesIO()
        if yt.check_availability() is None:
            url = yt.thumbnail_url
            title = yt.title
            updater.bot.sendPhoto(id, url, caption=title)
        else:
            update.message.reply_text('Xatolik ...')

updater = Updater(TOKEN)

youtube = Youtube()

# add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', youtube.start))
updater.dispatcher.add_handler(MessageHandler(Filters.entity('url'), youtube.text_sorch))
updater.dispatcher.add_handler(CallbackQueryHandler(youtube.get_audio, pattern='๐MP3'))
updater.dispatcher.add_handler(CallbackQueryHandler(youtube.get_vidoe,pattern='๐นdp'))
updater.dispatcher.add_handler(CallbackQueryHandler(youtube.get_img, pattern='๐ผ'))

#Start the bot
updater.start_polling()
updater.idle()