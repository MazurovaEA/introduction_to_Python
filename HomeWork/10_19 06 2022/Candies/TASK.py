# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# а) Добавьте игру против бота
# б) Подумайте как наделить бота "интеллектом"

from pickle import GLOBAL
from random import randint
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

total_candies = 50
max_candies = 8
gamer = 1
game_type = 0    # Переменная для выбора типа игры
gaming = False
# Определяем константы этапов разговора
# CHOICE, GAME = range(2)
CHOICE = 0

def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Человек', 'Умный компьютер', 'Не очень умный компьютер']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Начинаем игру! Выберите с кем хотите сыграть?'
        'Команда /cancel, чтобы прекратить игру.\n\n',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список 
    # обработчиков, определенных в виде значения ключа `GENDER`
    return CHOICE

# Обрабатываем выбор пользователя
def choice(update, context):
    # определяем выбор
    global game_type 
    game_type = update.message.text
    print(game_type)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    context.bot.send_message(update.effective_chat.id,
        'Поехали! (с)')
    context.bot.send_message(update.effective_chat.id,f'На столе лежит {total_candies} конфет')
    gaming = True
    context.bot.send_message(update.effective_chat.id, f'Введите количество конфет, которые вы берете (не более {max_candies}): ')
    return ConversationHandler.END

def cancel(update, _):
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться.'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

def message(update, context):
    global total_candies
    text = update.message.text
    if not text.isdigit() or int(text) == 0:
        context.bot.send_message(update.effective_chat.id, f'Вы ввели неправильное значение, попробуйте снова.') 
    elif int(text) > max_candies:
        context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше {max_candies}, попробуйте снова.')
    elif total_candies <= max_candies and int(text) > total_candies:
        context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше чем конфет на столе, попробуйте снова.')
    else:
        take_candies = int(text)
        total_candies = total_candies - take_candies
        print(total_candies)
        print(game_type)     
        if total_candies == 1:
            context.bot.send_message(update.effective_chat.id, f'Выиграл игрок')
            gaming = False
            return
        if game_type == 'Не очень умный компьютер':   
            if total_candies <= max_candies:
                take_candies = randint(1, total_candies)
            else:
                take_candies = randint(1, max_candies)
            context.bot.send_message(update.effective_chat.id, f'Ходит компьютер и берет {take_candies} конфет')
            total_candies = total_candies - take_candies
            context.bot.send_message(update.effective_chat.id, f'Осталось {total_candies} конфет')
            if total_candies == 1:
                context.bot.send_message(update.effective_chat.id, f'Выиграл компьютер')
                gaming = False
                return








# 'Человек', 'Умный компьютер', 'Не очень умный компьютер'


    # if X == 1 and gamer == 2:
    #     if Y == 0:
    #         if total_candies <= max_candies:
    #             take_candies = randint(1, total_candies)
    #         else:
    #             take_candies = randint(1, max_candies)
    #     else:
    #         if total_candies == max_candies:
    #             take_candies = max_candies-1
    #         elif total_candies < max_candies:
    #             take_candies = total_candies-1
    #         elif total_candies <= max_candies*2 and total_candies >= (max_candies+1):
    #             take_candies = total_candies % (max_candies+1)-1
    #             if take_candies <= 0:
    #                 take_candies = max_candies
    #         else:
    #             take_candies = total_candies % (max_candies+1)-1

    #     print(f'Ходит компьютер и берет {take_candies} конфет')
    # else:
    #     print(f'Ходит игрок №{gamer}')
    #     take_candies = enter_number()

    # total_candies = total_candies - take_candies
    # if total_candies > 1:
    #     print(f'Осталось {total_candies} конфет')
    #     if gamer == 1:
    #         gamer = 2
    #     else:
    #         gamer = 1
    # elif total_candies == 0:
    #     if gamer == 1:
    #         gamer = 2
    #     else:
    #         gamer = 1
    #     if X == 1 and gamer == 2:
    #         print(f'Победа компьютера!')
    #     else:
    #         print(f'Победа игрока №{gamer}')
    #     gaming = False
    # else:
    #     if X == 1 and gamer == 2:
    #         print(f'Осталась одна конфета! Победа компьютера!')
    #     else:
    #         print(f'Осталась одна конфета! Победа игрока №{gamer}')
    #     gaming = False

