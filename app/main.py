import telegram
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext
bot = telegram.Bot(token='YOUR_BOT_TOKEN')
from dotenv import load_dotenv
import openai

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('USERNAME')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

openai.api_key = OPENAI_API_KEY

app = ApplicationBuilder().token(BOT_TOKEN).build()


async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi there. I am your friendly bot. Type /help to see what I can do.')


async def send_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Here are some commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/echo <text> - I will repeat what you say!"
    )
    await update.message.reply_text(help_text)

async def get_ai_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
            logger.error(f"Error getting AI response: {e}")
            return "I'm sorry, but I couldn't process your request at this time."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logger.info(f"User message: {user_message}")
    
    ai_response = await get_ai_response(user_message)
    
    await update.message.reply_text(ai_response)



async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text_to_echo = ' '.join(context.args)  
        await update.message.reply_text(text_to_echo)
    else:
        await update.message.reply_text("Please provide text to echo.")


async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


async def catch_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sorry I do not understand what you wrote. Type /help for a list of commands.")


async def error_handler(update: Update, context: CallbackContext):
    logger.error(f'Update {update} caused error {context.error}')
    await update.message.reply_text("An error occurred. Please try again later.")
    

app.add_handler(CommandHandler("start", start_message))
app.add_handler(CommandHandler("help", send_help))
app.add_handler(CommandHandler("echo", echo_message))
app.add_handler(CommandHandler("text", echo_all))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_error_handler(error_handler)


if __name__ == "__main__":
    print('Bot starting...')
    app.run_polling()
