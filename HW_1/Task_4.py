'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:'''

from random import randint


def rand_game():

    attempts = 10
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000

    randint_num = randint(LOWER_LIMIT, UPPER_LIMIT)

    for i in range(attempts, 0, -1):

        a = int(input('Введите число: '))
        attempts -= 1

        if a == randint_num:
            print('Вы нашли загаданное число')
            break

        elif a < randint_num:
            print('Загаданное число больше чем введенное вами \nОсталось попыток:', attempts)

        else:
            print('Загаданное число меньше чем введенное вами \nОсталось попыток:', attempts)
    else:
        print('Вы исчерпали все попытки')
    print(randint_num, a)

rand_game()