'''Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».'''

N = int(input('Введите необходимое колисечтво простых чисел: '))

def isprime(num):
    k = 0
    if num == 1:
        return False
    for x in range(2, num // 2+1):
        if num % x == 0:
            k = k+1
    if (k<=0):
        return True
    else:
        return False

def primes(num = 1):
    while(True):
        if isprime(num):
            yield num
        num += 1

for i, j in enumerate(primes(), start=1):
    if i >= N + 1: break
    print(f'{i:<3}: {j:>3}')

