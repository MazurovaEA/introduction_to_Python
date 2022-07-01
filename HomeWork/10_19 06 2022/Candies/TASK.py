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
CHOICE = 0

def start(update, _):
    global total_candies, gamer, gaming
    total_candies = 50
    gamer = 1
    gaming = True
    # Список кнопок для ответа
    reply_keyboard = [['Человек', 'Умный компьютер', 'Не очень умный компьютер']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Начинаем игру! Выберите с кем хотите сыграть?'
        'Команда /cancel, чтобы прекратить игру.\n\n',
        reply_markup=markup_key,)

    return CHOICE

# Обрабатываем выбор пользователя
def message(update, context):
    # определяем выбор
    global game_type
    game_type = update.message.text
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    context.bot.send_message(update.effective_chat.id,
        'Поехали! (с)')
    context.bot.send_message(update.effective_chat.id,f'На столе лежит {total_candies} конфет')
    # gaming = True
    context.bot.send_message(update.effective_chat.id, f'Введите количество конфет, которые вы берете (не более {max_candies}): ')
    if game_type == 'Человек':
        context.bot.send_message(update.effective_chat.id, f'Сейчас ход игрока №{gamer}')
    return ConversationHandler.END

def cancel(update, _):
    # Отвечаем на отказ играть
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться.'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем игру.
    return ConversationHandler.END

def game(update, context):
    global total_candies, gamer, gaming
    text = update.message.text
    if not gaming:
        context.bot.send_message(update.effective_chat.id, f'Запустите игру командой старт')
        return 
    if game_type == 'Не очень умный компьютер' or game_type == 'Умный компьютер':  
        if not text.isdigit() or int(text) == 0:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели неправильное значение, попробуйте снова.') 
        elif int(text) > max_candies:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше {max_candies}, попробуйте снова.')
        elif total_candies <= max_candies and int(text) > total_candies:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше чем конфет на столе, попробуйте снова.')
        else:
            take_candies = int(text)
            total_candies = total_candies - take_candies
            if total_candies == 1:
                context.bot.send_message(update.effective_chat.id, f'Выиграл игрок')
                gaming = False
                # total_candies = 50
                return
            if total_candies == 0:
                context.bot.send_message(update.effective_chat.id, f'Выиграл компьютер')
                gaming = False
                # total_candies = 50
                return
        if game_type == 'Не очень умный компьютер':   
            if total_candies <= max_candies:
                take_candies = randint(1, total_candies)
            else:
                take_candies = randint(1, max_candies)
            context.bot.send_message(update.effective_chat.id, f'Ходит компьютер и берет {take_candies} конфет')
            total_candies = total_candies - take_candies
            context.bot.send_message(update.effective_chat.id, f'Осталось {total_candies} конфет')
            if total_candies <= 1:
                context.bot.send_message(update.effective_chat.id, f'Выиграл компьютер')
                gaming = False
                # total_candies = 50
                return
        elif game_type == 'Умный компьютер':   
            if total_candies == max_candies:
                take_candies = max_candies-1
            elif total_candies < max_candies:
                take_candies = total_candies-1
            elif total_candies <= max_candies*2 and total_candies >= (max_candies+1):
                take_candies = total_candies % (max_candies+1)-1
                if take_candies <= 0:
                    take_candies = max_candies
            else:
                take_candies = total_candies % (max_candies+1)-1
            context.bot.send_message(update.effective_chat.id, f'Ходит компьютер и берет {take_candies} конфет')
            total_candies = total_candies - take_candies
            context.bot.send_message(update.effective_chat.id, f'Осталось {total_candies} конфет')
            if total_candies == 1:
                context.bot.send_message(update.effective_chat.id, f'Выиграл компьютер')
                gaming = False
                # total_candies = 50
                return
    if game_type == 'Человек':
        if not text.isdigit() or int(text) == 0:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели неправильное значение, попробуйте снова.') 
        elif int(text) > max_candies:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше {max_candies}, попробуйте снова.')
        elif total_candies <= max_candies and int(text) > total_candies:
            context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше чем конфет на столе, попробуйте снова.')
        else:
            take_candies = int(text)
            total_candies = total_candies - take_candies
            context.bot.send_message(update.effective_chat.id, f'Осталось {total_candies} конфет')
            if total_candies == 1:
                context.bot.send_message(update.effective_chat.id, f'Выиграл игрок №{gamer}')
                gaming = False
                # total_candies = 50
                # gamer = 1
                return
            gamer = 2 if gamer == 1 else 1
            context.bot.send_message(update.effective_chat.id, f'Сейчас ход игрока №{gamer}')
            if total_candies == 0:
                context.bot.send_message(update.effective_chat.id, f'Выиграл игрок №{gamer}')
                gaming = False
                # total_candies = 50
                # gamer = 1
                return