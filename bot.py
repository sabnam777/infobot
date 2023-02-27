        # handling callback queries for premium button
        elif callback_query.data == 'premium':
            # Creating a message with premium page content
            premium_message = f"Buy premium to access exclusive content and features\n\n" \
                              f"Join our premium group: t.me/yourpremiugroup\n\n" \
                              f"Contact us for more details."
            bot.send_photo(chat_id=chat_id, photo=PREMIUM_IMAGE_URL, caption=premium_message)
            
            # Creating an inline keyboard with button to join premium group
            join_premium_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="Join Premium Group", url=PREMIUM_GROUP_URL)]])
            
            # Sending the keyboard to the user
            bot.send_message(chat_id=chat_id, text="Click below to join our premium group", reply_markup=join_premium_keyboard)
        
        # handling callback queries for donation button
        elif callback_query.data == 'donation':
            # Creating a message with donation page content
            donation_message = f"Support us by donating to our project\n\n" \
                                f"Your support will help us improve our services and bring new features.\n\n" \
                                f"UPI: example@upi\n" \
                                f"PhonePe: 9999999999\n" \
                                f"Paytm: 9999999999\n\n" \
                                f"Thank you for your support!"
            bot.send_photo(chat_id=chat_id, photo=DONATION_IMAGE_URL, caption=donation_message)
            
        # handling callback queries for broadcast button
        elif callback_query.data == 'broadcast':
            # Only the bot owner can use broadcast feature
            if chat_id != OWNER_CHAT_ID:
                bot.send_message(chat_id=chat_id, text="You are not authorized to use this feature!")
            else:
                # Creating a message for broadcast
                broadcast_message = f"Hello everyone, this is a broadcast message from the bot owner.\n\n" \
                                     f"Please ignore this message if it is not relevant to you."
                
                # Sending the broadcast message to all users who have started the bot
                for user_id in USERS:
                    bot.send_message(chat_id=user_id, text=broadcast_message)
                
                # Sending a confirmation message to the bot owner
                bot.send_message(chat_id=chat_id, text="Broadcast message sent to all users.")                    
