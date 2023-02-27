from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, InlineQueryResultArticle


# Create bot instance
bot = Client(
    "Donate",
    bot_token=os.environ["5932409230:AAEDKc0qnKR57rNXNWvu6cxmqAzZCAklhx4"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"])

# Define home page with three buttons
@bot.on_message(filters.command("start"))
def start(bot, update):
    chat_id = update.chat.id
    first_name = update.chat.first_name

    markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Join our group", url="t.me/your_group"),
            InlineKeyboardButton("Join our channel", url="t.me/your_channel")
        ],
        [InlineKeyboardButton("Buy premium", url="t.me/your_premium_group")]
    ])

    bot.send_message(
        chat_id=chat_id,
        text=f"Welcome {first_name}! Choose an option below:",
        reply_markup=markup
    )


# Redirect to group and channel
@bot.on_message(filters.regex(r"^Join our group$"))
def group(bot, update):
    chat_id = update.chat.id

    bot.send_message(
        chat_id=chat_id,
        text="Join our group: t.me/your_group"
    )

@bot.on_message(filters.regex(r"^Join our channel$"))
def channel(bot, update):
    chat_id = update.chat.id

    bot.send_message(
        chat_id=chat_id,
        text="Join our channel: t.me/your_channel"
    )

@bot.on_message(filters.regex(r"^Buy premium$"))
def premium(bot, update):
    chat_id = update.chat.id

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Join premium group", url="t.me/your_premium_group")]
    ])

    photo_url = "https://te.legra.ph/file/a92e3ce02ed084795a865.jpg"
    caption = "Unlock premium features now!"
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )

@bot.on_message(filters.command("donate"))
def donate(bot, update):
    chat_id = update.chat.id

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Pay with Paytm", url="https://paytm.me/your_paytm_link")],
        [InlineKeyboardButton("Pay with UPI", url="upi://pay?pa=your_upi_id")],
        [InlineKeyboardButton("Pay with PhonePe", url="https://www.phonepe.com/en/")]
    ])

    photo_url = "https://te.legra.ph/file/d9c29bfcfdaff38eb8a3a.jpg"
    caption = "Thank you for your donation!"
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )


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
owner_id = "5143506371"

@bot.on_message(filters.command("broadcast") & filters.user(owner_id))
def broadcast(bot, update):


# Start the bot
bot.polling()
