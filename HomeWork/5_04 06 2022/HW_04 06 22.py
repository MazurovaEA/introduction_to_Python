# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
# Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк абВ абырвалг'.split()
fragment = 'абв'

def del_word_by_fragm(text,fragment):
    '''
    Функция по нахождению фрагмента в слове (вне зависимости от регистра) и удалению этого слова
    '''
    new_words = [word for word in text if fragment not in word.casefold()]
    new_text = ' '.join(new_words)
    return(new_text)

print(del_word_by_fragm(text,fragment))

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

board = list(range(1,10))

def draw_board(board):
    print ('-' * 13)
    for i in range(3):
        print ('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print ('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input('Куда поставим ' + player_token+'? ')
        try:
            player_answer = int(player_answer)
        except:
            print ('Некорректный ввод. Попробуйте повторить')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ('Данная клеточка уже занята')
        else:
            print ('Некорректный ввод. Введите число от 1 до 9.')

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print ('Победила дружба!')
            break
    draw_board(board)

main(board)

# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин.
# Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма.
# Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин.
# В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем.
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо.
# Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть.
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

text = 'Ну, вышел я,  из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем.Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо.Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил'
bad_words = ['ну', 'В общем', 'короче говоря', 'кажется', 'иду я','ээ','_э' ,'короче,', ',кажется', 'в общем', 'ясен пень', 'как бы', 'кстати', 'короче', '... ,', '….','…', '...',', ,', ', _', '_,' ]

for word in bad_words:
    text = text.casefold().replace(word, '_')

text = text.replace('я,','я')
text = text.replace('_','')
text = text.replace('  ',' ')
text = text.split('.')

final_sentences = []
for sentence in text:
  sentence = sentence.strip()
  if not sentence:
    continue
  sentence = sentence.capitalize()
  final_sentences.append(sentence)

final_text = '. '.join(final_sentences)
final_text = final_text  + '.'
print(final_text)