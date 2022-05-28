# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

myList = [1, 2, 3, 6, 8, -4, 2, 1]
sum = 0
for item in range(1, len(myList), 2):
    sum += myList[item]
print('Сумма чисел, стоящих на нечетной позиции равна', sum)

# ****************************************************************************************************************
# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

Numbers = [2, 3, 4, 5, 6]
result = []
for i in range(0, round((len(Numbers)+0.1)/2)):
    result.append(Numbers[i]*Numbers[-1*i-1])
print(result)

# ***************************************************************************************************************
# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import decimal
myNumbers = [1.1, 1.2, 3.1, 5, 10.01]
newList = []
for i in range(len(myNumbers)):
    newList.append(myNumbers[i] - myNumbers[i]//1)
maxDigit = max(newList)
minDigit = min(newList)
res = maxDigit-minDigit
decimal_res = decimal.Decimal(str(res)).quantize(decimal.Decimal('.01'),
   rounding=decimal.ROUND_DOWN)
print(myNumbers)
print(f'{decimal_res}')

# ***************************************************************************************************************
# 4. Написать программу преобразования десятичного числа в двоичное

Number = int(input('Введите число => '))
newList = []
while (Number > 0):
    ans = int(Number % 2)
    newList.append(ans)
    Number = Number//2
temp = newList.reverse()
newString = str(newList)
for char in newString:
    if char in "[,] ":
        newString=newString.replace(char,"")
print(newString)
