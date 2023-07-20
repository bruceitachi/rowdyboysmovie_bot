import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token obtained from BotFather
BOT_TOKEN = "6345281756:AAG0r-_D_1Hl0io5u3VLEBI2z9FWMqDwC-A"

# List to store movie requests
movie_requests = []

# Command handlers
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your Movie Request Bot. Use /request to request a movie and /list to see all requests.")

def request_movie(update: Update, _: CallbackContext) -> None:
    movie_name = update.message.text[len('/request '):].strip()
    if movie_name:
        movie_requests.append(movie_name)
        update.message.reply_text(f"Your movie request for '{movie_name}' has been noted!")
    else:
        update.message.reply_text("Please provide a movie name after /request command.")

def list_requests(update: Update, _: CallbackContext) -> None:
    if movie_requests:
        update.message.reply_text("\n".join(movie_requests))
    else:
        update.message.reply_text("No movie requests yet.")

def unknown_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text("Sorry, I don't understand that command.")

def main() -> None:
    updater = Updater(6345281756:AAG0r-_D_1Hl0io5u3VLEBI2z9FWMqDwC-A)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("request", request_movie))
    dispatcher.add_handler(CommandHandler("list", list_requests))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
