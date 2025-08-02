from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Привет! Я работаю.")

updater = Updater("8353371506:AAGK1kl79KP3FTGaw0f9iCdgX7FM9Pfp3v4", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
