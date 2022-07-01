# 1. Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

value = input('Введите выражение: ')

def calculate(my_value):
    my_string = my_value[:]
    my_string = my_string.replace(' ', '') # убираем пробелы из строки
    start, end = None, None   #
    str_left, str_right = '',''
    count = my_string.count('(')
    while True:
        if count == 0:
            return calculate_arithm(my_string)
        for index in range(0, len(my_string)):  # Перебираем символы в строке по порядку. Ищем скобки
            if my_string[index] == '(':
                start = index
            if my_string[index] == ')':
                end = index
                break
        if start > 0:
            if my_string[start-1] == ')' or my_string[start-1].isdigit():
                str_left = '*'
        if end + 1 <= len(my_string)-1:
            if my_string[end+1] == '(' or my_string[end+1].isdigit():
                str_right = '*'
        my_string = my_string[:start] + str_left + calculate_arithm(my_string[start+1:end]) + str_right + my_string[end + 1:]

        count -= 1

def calculate_arithm(my_value):
    my_string = my_value[:]
    my_string = my_string.replace(' ', '')  
    start, end = None, None
    precision = 0
    for oper in ['*', '/', '+', '-']:  
        count = my_string.count(oper)       
        if count != 0:
            for i in range(0, count):   
                target = my_string.find(oper)
                step = 1
                dot = False
                while (target - step >= 0) and (my_string[target - step].isdigit() or my_string[target - step] == '.'): 
                    if my_string[target - step] == '.':
                        dot = True
                        if precision < step:
                            precision = step
                    step += 1
                step -= 1
                start = target - step
                if dot:
                    if my_string[start:target] == '':
                        a = 0
                    else:
                        a = float(my_string[start:target])
                else:
                    if my_string[start:target] == '':
                        a = 0
                    else:
                        a = int(my_string[start:target])
                step = 1
                dot = False
                pred_prec = 0
                while (target + step < len(my_string)) and (my_string[target + step].isdigit() or my_string[target + step] == '.' or my_string[target + 1] == '-'):
                    if my_string[target + step] == '.':
                        dot = True
                        pred_prec = step
                    step += 1
                step -= 1
                end = target + step
                if precision < (end - pred_prec):
                    precision = end - pred_prec
                if dot:
                    b = float(my_string[target+1:end + 1])
                else:
                    b = int(my_string[target+1:end + 1])
                if oper == '*':
                    res = str(a*b)
                if oper == '/':
                    res = str(a/b)
                if oper == '+':
                    res = str(a+b)
                if oper == '-':
                    res = str(a-b)
                my_string = my_string[0:start] + res + my_string[end+1:]
    return my_string

print(calculate(value))

# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах 
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

text = """Юра вошел в автобус и сел на детское место. Вслед за Юрой вошел военный. Юра вскочил:
— Садитесь, пожалуйста!
— Сиди, сиди! Я вот здесь сяду.
Военный сел сзади Юры. По ступенькам поднялась старушка.
Юра хотел предложить ей место, но другой мальчик опередил его.
«Некрасиво получилось», — подумал Юра и стал зорко смотреть на дверь.
С передней площадки вошла девочка. Она прижимала к себе туго свернутое байковое одеяльце, из которого торчал кружевной чепчик.
Юра вскочил:
— Садитесь, пожалуйста!
Девочка кивнула головой, села и, раскрыв одеяло, вытащила большую куклу.
Пассажиры засмеялись, а Юра покраснел.
— Я думал, она женщина с ребенком, — пробормотал он.
Военный одобрительно похлопал его по плечу:
— Ничего, ничего! Девочке тоже надо уступать место! Да еще девочке с куклой!"""

path1 = 'text_for_encode.txt'
path2 = 'text_for_decode.txt'
with open(path1, 'w') as data:
    data.write(text)
    
def encode_text(name_file_in, name_file_out):
    res = ''
    old_char = ''
    count = 1
    with open(name_file_in, 'r') as data:
        for lines in data.readlines() :
            for char in lines:
                if char != old_char or count == 9:
                    if old_char:
                        res += str(count) + old_char
                    old_char = char
                    count = 1
                else:
                    count += 1
        else:
            res += str(count) + old_char
            with open(name_file_out, 'w') as data:
                data.write(res)


def decode_text(name_file):
    step = 0
    count = 0
    res = ''
    with open(name_file,'r') as data:
        for lines in data.readlines() :
            for char in lines:
                if step == 0:
                    count = int(char)
                else:
                    res += count * char
                step = (step + 1) % 2
        return res


encode_text(path1, path2)
print(decode_text(path2))

# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. 
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

path1 = 'text_for_encode_ROT13.txt'
path2 = 'text_for_decode_ROT13.txt'
with open(path1, 'w') as data:
    data.write(text)

def encode_ROT13(line):
    res = ''
    enc_alpha = 'abcdefghijklmnopqrstuvwxyz'
    for symb in line:
        dig = enc_alpha.find(symb.lower())
        if dig != -1:
            char = enc_alpha[(dig + 13)%26]
        else:
            char = symb
        res += char
    return res


print(encode_ROT13(text))                   
print(encode_ROT13(encode_ROT13(text)))     