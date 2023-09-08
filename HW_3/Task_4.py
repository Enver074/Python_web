"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака."""

import random

things_for_the_trip = {'вода': 2500, 'крупа': 1500, 'фрукты': 1500, 'куртка': 500,
                       'термос': 2000, 'бинокль': 500, 'компас': 100, 'чайник': 1000,
                       'джинсы': 500, 'камера': 1500, 'котелок': 1500, 'миска': 250,
                       'ложка': 50, 'вилка': 50, 'нож': 50, 'топор': 1000, 'кружка': 70,
                       'соль': 70, 'фонарик': 250, 'зажигалка': 50, 'репшнур': 100,
                       'гитара': 1500, 'ботинки': 1000, 'швейный набор': 70, 'сидушка': 70,
                       'палатка': 2000, 'спальный мешок': 1000, }

capacity = int(input("Введите вместимость рюкзака: "))


# функция вывода вместимости рюкзака и вещей в рюкзаке
def print_backpack(backpack_capacity, current_capacity, things_in_backpack):
    print(f'Вместимость рюкзака: {backpack_capacity}, использованный вес: {current_capacity}')
    print("---" * 8)

    len_max_item = max(things_in_backpack, key=len)
    len_max_item = len(len_max_item) + 1

    for i, weight in things_in_backpack.items():
        print(f'{i:<{len_max_item}}: {weight :>5}')

    print("---" * 8)


# функция сортировки вещей по весу
def backpack_sorted(items):
    sorted_things = dict(sorted(items.items(), key=lambda x: x[1],
                                reverse=True))  # сортировка вещей по весу, от большего к меньшему

    return sorted_things

# функция перемешивания вещей
def backpack_shuffled(items):

    key_list = list(items)  # создал список вещей
    random.shuffle(key_list)  # перемешал

    shuffle_things = {}  # создал пустой словарь
    for key in key_list:  # заполнил словарь перемешанными вещами
        shuffle_things[key] = things_for_the_trip[key]

    return shuffle_things

# функция сборки вещей в рюкзак
def backpack(data, things):

    print(data)

    backpack_capacity = capacity        # вместимость рюкзака
    current_capacity = 0                # текущая вместимость

    things_in_backpack = {}             # создал пустой словарь

    for i, value in things.items():     # заполнил словарь вещами
        if backpack_capacity >= (current_capacity + value):
            things_in_backpack[i] = value
            current_capacity += value

    print_backpack(backpack_capacity, current_capacity, things_in_backpack)



if __name__ == "__main__":
    backpack('Отсортированные вещи по весу', backpack_sorted(things_for_the_trip))
    backpack('Перемешанные вещи', backpack_shuffled(things_for_the_trip))