"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions"""
import fractions


def main():
    a = str(input("Введите простую дробь(“a/b”): "))
    b = str(input("Введите простую дробь(“c/d”): "))

    print(fract_calc(a, b))
    print(check(a, b))

# проверка через функцию 'Fractions'
def check(a, b):
    if "/" in a and "/" in b:
        number_split = a.split("/") + b.split("/")
        fraction_1 = fractions.Fraction(int(number_split[0]), int(number_split[1]))
        fraction_2 = fractions.Fraction(int(number_split[2]), int(number_split[3]))

        return f'Проверка Fractions сумма {fraction_1 + fraction_2}, произведение {fraction_1 * fraction_2}'

    else:
        return "Введите простую дробь(“a/b”): "

# получение числителей и знаменателей из дробей
def fract_split(a: str,b: str):
    if "/" in a and "/" in b:
        number_split = a.split("/") + b.split("/")
        a, b, c, d = int(number_split[0]), int(number_split[1]), int(number_split[2]), int(number_split[3])
        return a, b, c, d

    else:
        print("Введите простую дробь(“a/b”): ")

# сложение и произведение дробей
def fract_calc(a, b):
    a, b, c, d = fract_split(a, b)

    # наименьшее общее кратное
    common_denominator = lcm(b, d)

    # приведение к общему знаменателю
    a *= common_denominator // b
    b = common_denominator
    c *= common_denominator // d
    d = common_denominator

    # сложение числителя
    num_sum = a + c

    # наибольший общий делитель
    common_factor_sum = gcd(num_sum, common_denominator)

    # сокращение
    num_sum //= common_factor_sum
    common_denominator //= common_factor_sum

    # перемножение дробей
    num = a * c
    den = b * d

    # наибольший общий делитель
    common_factor_mult = gcd(num, den)

    # сокращение
    num //= common_factor_mult
    den //= common_factor_mult

    return f'Сумма дробей равна: {num_sum}/{common_denominator}, Произведение дробей равно: {num}/{den}'


# поиск наибольшего общий делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#поиск наименьшого общего кратного
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    main()
