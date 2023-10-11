import telebot
from handlers import handle_start, handle_help
from dotenv import load_dotenv
import os

# Store your API key in a .env file in the same folder
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    handle_start(bot, message)
    
@bot.message_handler(commands=['help'])
def start(message):
    handle_help(bot, message)

bot.polling()
