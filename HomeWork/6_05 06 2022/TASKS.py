# 1. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
#  *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from email import policy
from random import randint

def printPoli(k, koef_list):
    poli = ''
    for i, j in enumerate(koef_list):
        if (k-i != 0 and j == 0):
            continue
        elif (k-i == 0 and j == 0):
            poli += (f' = 0')
        elif (k-i == 0 and j != 0):
            poli += (f' + {j} = 0')
        elif (k-i == 1 and j == 1):
            poli += (' + x')
        elif (k-i == 1 and j != 1):
            poli += (f' + {j}*x')
        elif (k-i > 1 and j == 1):
            poli += (f' + x^{k-i}')
        elif (i == 0 and j > 1):
            poli += (f'{j}*x^{k-i}')
        elif (i == 0 and j == 1):
            poli += (f'x^{k-i}')
        else:
            poli += (f' + {j}*x^{k-i}')
    return poli

k = int(input('Введите k: '))
koef_list = []
for i in range(0, k+1):
    if (i == 0):
        koef_list.append(randint(1, 2))
    else:
        koef_list.append(randint(0, 2))

path = 'file.txt'
with open(path, 'w') as data:
    data.write(f'{printPoli(k,koef_list)}')

print(koef_list)

# 2. Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.
# (два файла, ответ в третьем файле)

def readData(path):              
    data = open(path, 'r')
    for line in data:
        s = line
    data.close()
    return s

def Dictionary(s: str):
    s = s.replace('= 0', '')
    s = s.replace(' ', '')
    list = s.split('+')
    dict = {}
    for i in list:
        kursor = i.find('x')
        if(kursor == -1):
            dict['0'] = int(i)       # то берём значение строки
        elif(kursor == len(i)-1):             # Если первая степень х
            dict['1'] = int(i[0:kursor-1])
        else:
            if(kursor == 0):
                dict[i[kursor + 2:]] = 1
            else:
                dict[i[kursor + 2:]] = int(i[0:kursor-1])
    return dict

def sumDict(dictionary1, dictionary2):
    dictionary1_keys, dictionary2_keys = dictionary1.keys(), dictionary2.keys()
    set_of_dict, total_dict = set(dictionary1.keys()).union(
        set(dictionary2.keys())), {}
    for key in set_of_dict:
        if key in dictionary1_keys and key in dictionary2_keys:
            total_dict[key] = dictionary1[key] + dictionary2[key]
        elif key in dictionary1:
            total_dict[key] = dictionary1[key]
        else:
            total_dict[key] = dictionary2[key]
    return total_dict

def printPoli(newDict):
    poli = ''
    for key in newDict:
        if (key == max(newDict.keys()) and newDict[key] != 1):
            poli += (f'{newDict[key]}*x^{key}')
        elif (key == max(newDict.keys()) and newDict[key] == 1):
            poli += (f'x^{key}')
        elif (key < max(newDict.keys()) and key != '0' and key != '1' and newDict[key] != 1):
            poli += (f' + {newDict[key]}*x^{key}')
        elif (key < max(newDict.keys()) and key != '0' and key != '1' and newDict[key] == 1):
            poli += (f' + x^{key}')
        elif (key == '0'):
            poli += (f' + {newDict[key]} = 0')
        elif (key == '1'):
            poli += (f' + {newDict[key]}*x')
    return poli

path1 = 'file.txt'
path2 = 'file1.txt'
path3 = 'answer.txt'

print(readData(path1))
print(readData(path2))

newString1 = Dictionary(readData(path1))
newString2 = Dictionary(readData(path2))

print(newString1)
print(newString2)
print()
newDict = sumDict(newString1, newString2)
sorted_newDict = dict(sorted(newDict.items(), reverse= True)) #сортировка словаря по ключу от большего к меньшему
print(sorted_newDict)

print(printPoli(sorted_newDict))

with open(path3, 'w') as data:
    data.write(f'{printPoli(sorted_newDict)}')