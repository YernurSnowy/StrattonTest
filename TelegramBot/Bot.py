# Importing the libraries we need
import config
import telebot
from pymongo import MongoClient
from datetime import datetime

# Connection to MongoDB
db_client = MongoClient(config.mongo_uri)
db = db_client['telegram_bot']
collection = db['messages']

# Connect to Telegram Bot
bot = telebot.TeleBot(config.token)
print('Link to the Bot: t.me/EchoTaskBot')

# Function to repeat messages
@bot.message_handler(content_types=["text"])
def repeat_messages(message): 
    bot.send_message(message.chat.id, "Strattonbot " + message.text)

    # Add data to DB
    message_data = {
        "text": message.text,
        "date": datetime.now()
    }
    collection.insert_one(message_data)

# Start an endless loop of receiving new records
if __name__ == '__main__':
     bot.infinity_polling()

