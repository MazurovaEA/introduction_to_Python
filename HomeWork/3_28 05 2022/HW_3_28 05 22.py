# 1. Найти НОК двух чисел

def findNOD(a,b):
    if b == 0:
        return a
    return findNOD(b, a%b)

number1 = int(input('Введите первое число => '))
number2 = int(input('Введите второе число => '))

print(number1*number2//findNOD(number1,number2))

# 2. Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

import math

d = float(input('Задайте точность для числа пи '))
if (d >0.1 or d == 0 and d !=1):
    print('Ошибка задания точности!')
else:
    print (math.pi - math.pi % d)

# 3. Составить список простых множителей натурального числа N

import math

def prime_factors(num):
    my_list = []
    while num % 2 == 0:
        my_list.append(2)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            my_list.append(i)
            num = num / i
    if num > 2:
        my_list.append(int(num))
    return my_list

num = int(input('Введите натуральное число: '))
print(prime_factors(num))

# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = list(set(my_list))
print(new_list)

# + на тему файловой системы:
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.
path = 'file.txt'
f = open(path, 'r')
data = f.read()+' '
f.close()

# # создаем список из чисел в файле
numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

# # создаем выборку из нечетных элементов
answer = [e for e in numbers if e % 2]
# # записываем в файл
with open(path,'w') as data:
    data.write(" ".join(map(str, answer)))
