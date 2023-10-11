def handle_start(bot, message):
    bot.send_message(message.chat.id, "Welcome to the Expense Tracker bot!\nType /help to see all available commands.")
    
def handle_help(bot, message):
    help_text = """Here are the available commands:
    /start - To start the bot
    /help - To list all available commands"""
    bot.send_message(message.chat.id, help_text)
