"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""


def find_duplicates(lst):
    return list(set([i for i in lst if lst.count(i) > 1]))

lst = (1, 1, 1, 2, 3, 4, 5, 4, 6, 'a', 'c', 'a', 'b')

print(find_duplicates(lst))
