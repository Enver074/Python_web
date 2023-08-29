# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def multiply():
    print('ТАБЛИЦА УМНОЖЕНИЯ')
    for i in [2, 6]:
        for j in range(2, 11):
            q, w, e = i + 1, i + 2, i + 3

            print(f'{i}*{j}={i * j}\t{q}*{j}={q * j}\t{w}*{j}={w * j}\t{e}*{j}={e * j}'.expandtabs(10))

        print('')


multiply()