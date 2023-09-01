"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

def hexadecimal():
    decimal_number = int(input("Введите десятичное число: "))
    hexadecimal_digits = "0123456789abcdef"
    hexadecimal_number = ""

    # проверка через функцию hex
    hex_number = hex(decimal_number)[2:]

    while decimal_number > 0:
        remainder = decimal_number % 16  # Получаем остаток от деления на 16
        hexadecimal_digit = hexadecimal_digits[remainder]  # Получаем шестнадцатеричную цифру
        hexadecimal_number = hexadecimal_digit + hexadecimal_number  # Добавляем цифру в начало шестнадцатеричного числа
        decimal_number //= 16  # Выполняем целочисленное деление на 16

    print('Шестнадцатеричное число:', hexadecimal_number)
    print('Проверка:', hex_number)

if __name__ == "__main__":
    hexadecimal()
