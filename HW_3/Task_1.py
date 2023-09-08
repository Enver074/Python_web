"""✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

things_for_the_trip = {'Вася': ('вода', 'фонарик', 'вилка', 'еда', 'зажигалка', 'спальный мешок',
                                'палатка', 'миска', 'кружка', 'сменная одежда'),
                       'Петя': ('вода', 'компас', 'вилка', 'еда', 'фонарик', 'спальный мешок',
                                'камера', 'швейный набор', 'миска', 'кружка', 'сменная одежда'),
                       'Леша': ('вода', 'гитара', 'вилка', 'еда', 'нож', 'спальный мешок',
                                'репшнур', 'термос', 'миска', 'кружка', 'котелок', 'сменная одежда')}


def three_friends():


    all_things = set(things_for_the_trip['Вася']) & \
                 set(things_for_the_trip['Петя']) & \
                 set(things_for_the_trip['Леша'])

    unique_things = set(things_for_the_trip['Вася']) ^ \
                    set(things_for_the_trip['Петя']) ^ \
                    set(things_for_the_trip['Леша'])

    common_things = (
                        set(things_for_the_trip['Вася']) |
                        set(things_for_the_trip['Петя']) |
                        set(things_for_the_trip['Леша'])
                    ) - set(things_for_the_trip['Вася']), (
                        set(things_for_the_trip['Вася']) |
                        set(things_for_the_trip['Петя']) |
                        set(things_for_the_trip['Леша'])
                    ) - set(things_for_the_trip['Петя']), (

                        set(things_for_the_trip['Вася']) |
                        set(things_for_the_trip['Петя']) |
                        set(things_for_the_trip['Леша'])
                    ) - set(things_for_the_trip['Леша'])

    missing_things = {}

    names = list(things_for_the_trip)

    for things, name in zip(common_things, names):
        for thing in things:
            missing_things[thing] = name

    print(all_things)
    print(unique_things)
    print(missing_things)


if __name__ == "__main__":
    three_friends()
