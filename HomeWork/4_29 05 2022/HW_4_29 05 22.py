# Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

from itertools import combinations

my_list = [1, 5, 2, 3, 4, 6, 1, 7]
answer = []
ans_max = 0

def seq(my_list):   
    ans_max = 0
    for volume in my_list:
        if(volume > ans_max):
            ans_max = volume
        else:
            return False
    return True

for part in range(len(my_list)-1, 2, -1):   
    for item in combinations(my_list, part):
        if seq(item):
            print(item)
            exit()
print(answer)

# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

from random import randint

with open('file.txt','w') as data:
    numbers=[]
    for i in range(10):
        numbers.append(randint(1,100))
        data.write(str(numbers[i])+' ')

with open('file.txt','r') as file:
    data = file.read().split()

data.sort()

with open('file.txt','w') as file:
    for numbers in data:
        file.write(numbers+' ')

# Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

path = '1Kints.txt'

with open(path, 'r') as file:
    input_list = file.readlines()
    input_list.pop()
    list_of_volume = list(map(int, input_list))

count = 0

for first_volume in list_of_volume:
    for second_volume in list_of_volume:
        for third_volume in list_of_volume:
            if(first_volume + second_volume + third_volume == 0):
                print(f'{first_volume} + {second_volume} + {third_volume} = 0')
                count += 1
print(f'Количество триплетов = {count}')