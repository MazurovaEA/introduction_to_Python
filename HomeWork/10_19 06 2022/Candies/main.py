from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from TASK import *

path_file_token = 'C:\oken.txt'    # Считывает токен Телеграм-бота из текстового файла
with open(path_file_token, 'r') as data:
    for line in data:
        str_token = line

bot = Bot(token=str_token)
updater = Updater(token=str_token, use_context=True)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.regex('^(Человек|Умный компьютер|Не очень умный компьютер)$'), message)],
        },
        # точка выхода из игры
        fallbacks=[CommandHandler('cancel', cancel)],
    )

message_handler = MessageHandler(Filters.text, game)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)

# Запуск бота
print("Программа запущена!")
updater.start_polling()
updater.idle()