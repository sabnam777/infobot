import telebot
from telebot import types

# Create bot instance
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Define home page with three buttons
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    group_btn = types.KeyboardButton('Join our group')
    channel_btn = types.KeyboardButton('Join our channel')
    premium_btn = types.KeyboardButton('Buy premium')
    markup.add(group_btn, channel_btn, premium_btn)
    bot.send_message(message.chat.id, "Welcome! Choose an option below:", reply_markup=markup)

# Redirect to group and channel
@bot.message_handler(func=lambda message: message.text == 'Join our group')
def group(message):
    bot.send_message(message.chat.id, "Join our group: t.me/your_group")

@bot.message_handler(func=lambda message: message.text == 'Join our channel')
def channel(message):
    bot.send_message(message.chat.id, "Join our channel: t.me/your_channel")

# Redirect to premium page
@bot.message_handler(func=lambda message: message.text == 'Buy premium')
def premium(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Join premium group', url='t.me/your_premium_group')
    markup.add(button)
    photo_url = 'https://te.legra.ph/file/a92e3ce02ed084795a865.jpg'
    caption = 'Unlock premium features now!'
    bot.send_photo(message.chat.id, photo_url, caption=caption, reply_markup=markup)

# Donation page
@bot.message_handler(commands=['donate'])
def donate(message):
    markup = types.InlineKeyboardMarkup()
    paytm_btn = types.InlineKeyboardButton(text='Pay with Paytm', url='https://paytm.me/your_paytm_link')
    upi_btn = types.InlineKeyboardButton(text='Pay with UPI', url='upi://pay?pa=your_upi_id')
    phonepay_btn = types.InlineKeyboardButton(text='Pay with PhonePe', url='https://www.phonepe.com/en/')
    markup.add(paytm_btn, upi_btn, phonepay_btn)
    photo_url = 'https://te.legra.ph/file/d9c29bfcfdaff38eb8a3a.jpg'
    caption = 'Thank you for your donation!'
    bot.send_photo(message.chat.id, photo_url, caption=caption, reply_markup=markup)

# Broadcast feature for owner
owner_id = 'YOUR_TELEGRAM_ID'
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.chat.id == owner_id:
        bot.send_message(owner_id, "What message would you like to broadcast?")
        bot.register_next_step_handler(message, broadcast_message)

def broadcast_message(message):
    for chat in bot.chat_ids:
        if chat != owner_id:
            bot.send_message(chat, message.text)

# Start the bot
bot.polling()
