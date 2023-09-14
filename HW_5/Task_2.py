'''Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.'''

import os


def file_info(path):
    head, tail = os.path.split(path)
    name, extension = tail.split('.')
    return head, name, extension


path = '/Users/kalishka82/PyCharmProjects/GB_Jumping_In_Python/ht_04_functions/ex_01.py'

print(file_info(path))