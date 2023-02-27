import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Create bot instance
bot = Client(
    "Donate",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"]
)

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
        [InlineKeyboardButton("Premium", callback_data="premium")],
        [InlineKeyboardButton("Donate", callback_data="donate")]
    ])

    photo_url = "https://te.legra.ph/file/6750eaff7ac29676dbb31.jpg"
    caption = f"Welcome {first_name}! Choose an option below:"
    bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup
    )

# Premium page
@bot.on_callback_query(filters.regex("premium"))
def premium(bot, update):
    chat_id = update.message.chat.id

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

# Donation page
@bot.on_callback_query(filters.regex("donate"))
def donate(bot, update):
    chat_id = update.message.chat.id

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

# Broadcast feature for owner
owner_id = "1234567890"

@bot.on_message(filters.command("broadcast") & filters.user(owner_id))
def broadcast(bot, update):
    # Add your broadcast code here
    pass


# Start the bot
bot.run()
