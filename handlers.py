# handlers.py
from telebot import types
import csv

# Constants
CSV_FILENAME = "expenses.csv"
FIELDS = ['date', 'description', 'category', 'payment_method', 'amount']

def save_to_csv(data):
    """Save data to a CSV file."""
    with open(CSV_FILENAME, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(data)

# Step Functions
def process_date_step(message):
    chat_id = message.chat.id
    date = message.text
    msg = bot.send_message(chat_id, "Describe this expenditure.")
    bot.register_next_step_handler(msg, process_description_step, {'date': date})

def process_description_step(message, data):
    chat_id = message.chat.id
    description = message.text
    data['description'] = description
    markup = types.ReplyKeyboardMarkup(row_width=4)
    markup.add('Food', 'Transport', 'Groceries', 'Household', 'Utilities', 'Self', 'Gym/Exercise', 'Social')
    msg = bot.send_message(chat_id, "Please give this expenditure a category.", reply_markup=markup)
    bot.register_next_step_handler(msg, process_category_step, data)

def process_category_step(message, data):
    chat_id = message.chat.id
    category = message.text
    data['category'] = category
    markup = types.ReplyKeyboardMarkup(row_width=4)
    markup.add('UOB CC', 'Citi CC', 'Cash', 'OCBC')
    msg = bot.send_message(chat_id, "How did you pay for this expenditure?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_payment_method_step, data)

def process_payment_method_step(message, data):
    chat_id = message.chat.id
    payment_method = message.text
    data['payment_method'] = payment_method
    markup = types.ReplyKeyboardRemove()
    msg = bot.send_message(chat_id, "How much was spent? Please enter only numbers.", reply_markup=markup)
    bot.register_next_step_handler(msg, process_amount_step, data)

def process_amount_step(message, data):
    chat_id = message.chat.id
    amount = message.text
    data['amount'] = amount
    bot.send_message(chat_id, f"The following expense was added:\nDate: {data['date']}\nDescription: {data['description']}\nCategory: {data['category']}\nPayment Method: {data['payment_method']}\nAmount: {data['amount']}")
    save_to_csv(data)

# Command Handlers
def start(message):
    bot.send_message(message.chat.id, "Welcome to the Expense Tracker bot!\nType /help to see all available commands.")

def help(message):
    bot.send_message(message.chat.id, "Here are the available commands:\n/start - To start the bot\n/help - To list all available commands\n/add - To add an expense")

def add(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "When did you incur this expense?\nPlease give your answer in DD-MM-YYYY format.")
    bot.register_next_step_handler(msg, process_date_step)

def register_handlers(bot_instance):
    global bot
    bot = bot_instance
    bot.message_handler(commands=['start'])(start)
    bot.message_handler(commands=['help'])(help)
    bot.message_handler(commands=['add'])(add)
