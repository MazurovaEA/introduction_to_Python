from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from TASK import *

# path_file_token = 'token.py'    # Считывает токен Телеграм бота из текстового файла
# with open(path_file_token, 'r') as data:
#     for line in data:
#         str_token = line

bot = Bot(token='TOKEN')
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler( # здесь строится логика игры
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.regex('^(Человек|Умный компьютер|Не очень умный компьютер)$'), choice)],
            # GAME: [MessageHandler(Filters.text & ~Filters.command, game)],
        },
        # точка выхода из игры
        fallbacks=[CommandHandler('cancel', cancel)],
    )

message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)

# Запуск бота
print("Программа запущена!")
updater.start_polling()
updater.idle()