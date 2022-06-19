# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# а) Добавьте игру против бота
# б) Подумайте как наделить бота "интеллектом"
from random import randint

total_candies = 50
max_candies = 8
gamer = 1

X = int(input('Выберите с кем хотите играть (1 - компьютер, 0 - человек): '))
if X == 1:
    Y = int(input(
        'С каким компьютером вы хотите сыграть? (1 - очень умный, 0 - не очень :-) ): '))

def enter_number():
    err = True
    while err:
        N = input(
            f'Введите количество конфет, которые вы берете (не более {max_candies}): ')
        if not N.isdigit() or int(N) == 0:
            print(f'Вы ввели неправильное значение, попробуйте снова.')
        elif int(N) > max_candies:
            print(f'Вы ввели значение больше {max_candies}, попробуйте снова.')
        elif total_candies <= max_candies and int(N) > total_candies:
            print(f'Вы ввели значение больше чем конфет на столе, попробуйте снова.')
        else:
            err = False
            N = int(N)
    return N


end = True
print(f'На столе лежит {total_candies} конфет')
while end:
    if X == 1 and gamer == 2:
        if Y == 0:
            if total_candies <= max_candies:
                take_candies = randint(1, total_candies)
            else:
                take_candies = randint(1, max_candies)
        else:
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

        print(f'Ходит компьютер и берет {take_candies} конфет')
    else:
        print(f'Ходит игрок №{gamer}')
        take_candies = enter_number()

    total_candies = total_candies - take_candies
    if total_candies > 1:
        print(f'Осталось {total_candies} конфет')
        if gamer == 1:
            gamer = 2
        else:
            gamer = 1
    elif total_candies == 0:
        if gamer == 1:
            gamer = 2
        else:
            gamer = 1
        if X == 1 and gamer == 2:
            print(f'Победа компьютера!')
        else:
            print(f'Победа игрока №{gamer}')
        end = False
    else:
        if X == 1 and gamer == 2:
            print(f'Осталась одна конфета! Победа компьютера!')
        else:
            print(f'Осталась одна конфета! Победа игрока №{gamer}')
        end = False