import telegram
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
bot = telegram.Bot(token='YOUR_BOT_TOKEN')
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

app = ApplicationBuilder().token(BOT_TOKEN).build()


async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your friendly bot. Type /help to see what I can do.')


async def send_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are some commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/echo <text> - I will repeat what you say!"
    )
    await update.message.reply_text(help_text)


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text_to_echo = ' '.join(context.args)  
        await update.message.reply_text(text_to_echo)
    else:
        await update.message.reply_text("Please provide text to echo.")


async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


app.add_handler(CommandHandler("start", start_message))
app.add_handler(CommandHandler("help", send_help))
app.add_handler(CommandHandler("echo", echo_message))
app.add_handler(CommandHandler("text", echo_all))


if __name__ == "__main__":
    app.run_polling(none_stop=True)
