# main.py
from telebot import TeleBot
from dotenv import load_dotenv
import os
import handlers

# Initialize bot and load environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = TeleBot(API_KEY)

# Register handlers
handlers.register_handlers(bot)

# Start polling
bot.polling()
