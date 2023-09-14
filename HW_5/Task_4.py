'''Создайте функцию генератор чисел Фибоначчи (см. Википедию)'''

def fibonacci():
    num_1 = num_2 = 1
    while True:
        num_1, num_2 = num_2, num_1 + num_2
        yield num_2


my_iter = iter(fibonacci())

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))