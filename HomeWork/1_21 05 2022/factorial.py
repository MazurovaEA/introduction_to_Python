# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

n = int(input('Введите N => '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')