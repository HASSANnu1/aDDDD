import telebot
import time
import requests
from bs4 import BeautifulSoup

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual bot token
bot = telebot.TeleBot('6208733344:AAFniwxfyd-PluzqzVCpWAYwcsl2e65z7UE')

# Replace YOUR_CHANNEL_ID with your actual channel id
channel_id = -1001686953791
# Function to get the current Bitcoin price
def get_latest_crypto_price(coin):
    url = 'https://www.google.com/search?q=' + (coin) + 'price'
    # make a request to the website
    HTML = requests.get(url)
    # Parsse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser')
    # find the current price
    texti = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).find({
        'div': 'BNeawe iBp4i AP7Wnd'
    }).text
    return texti

# Function to send the Bitcoin price to the specified channel
def send_bitcoin_price():
    price = get_latest_crypto_price('bitcoin')
    bot.send_message(channel_id, f'Current Bitcoin price: {price}')

# Function to start the bot
def start_bot():
    bot.send_message(channel_id, 'Starting Bitcoin price updates...')
    while True:
        send_bitcoin_price()
        time.sleep(3600) # Sleep for 60 minutes (3600 seconds)

# Function to stop the bot
def stop_bot():
    bot.send_message(channel_id, 'Stopping Bitcoin price updates...')
    bot.stop_polling()

# Start the bot when the /start command is received
@bot.message_handler(commands=['start'])
def start_command(message):
    if message.chat.id == 1255788882:
        start_bot()

# Stop the bot when the /stop command is received
@bot.message_handler(commands=['stop'])
def stop_command(message):
    stop_bot()

# Start the bot
bot.polling()
