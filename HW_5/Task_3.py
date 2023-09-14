'''Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии'''

names: str =['Вася', 'Петя', 'Миша']
rates: int =[40_000, 80_000, 70_000]
awards: str =['10.25', '9.75', '11.30']

awards_sum = {name: rate * float(award[:-1]) for name, rate, award in zip(names, rates, awards)}

print(awards_sum)