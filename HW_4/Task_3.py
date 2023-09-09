"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
 Дополнительно сохраняйте все операции поступления и снятия средств в список."""

balance = 0  # текущий баланс
count = 0  # счетчик транзакций
percent_withdrawal = 1.5  # процент на снятие наличных
percent_operation = 3  # процент после каждой 3 транзакции
wealth_tax = 10  # налог на богатство


def program():
    global balance
    global count
    menu()
    command = str(get_transaction())

    while command != "4":
        if command == "1":
            amount = float(input("Пополнение баланса "))

            if count != 0 and count % 3 == 0:
                balance = balance + (percent_operation * amount) / 100
                print("Начислены проценты в размере: ", (percent_operation * amount) / 100)

            replenishment(amount)

            if balance > 5_000_000:
                balance = balance - (balance * wealth_tax) / 100
                print("Списан налог на богатство: ", (balance * wealth_tax) / 100)

            print("Ваш текущий баланс", format_currency(balance))
            menu()
            command = str(get_transaction())

        elif command == "2":
            amount = float(input("Снятие наличных "))

            if count != 0 and count % 3 == 0:
                balance = balance + (percent_operation * amount) / 100
                print("Начислены проценты в размере: ", (percent_operation * amount) / 100)

            withdrawal(amount)

            if balance > 5_000_000:
                balance = balance - (balance * wealth_tax) / 100
                print("Списан налог на богатство: ", (balance * wealth_tax) / 100)

            print("Ваш текущий баланс", format_currency(balance))
            menu()
            command = str(get_transaction())

        elif command == "3":
            print("Ваш текущий баланс", format_currency(balance))
            menu()
            command = str(get_transaction())

        else:
            print("Некорректная команда, попробуйте снова: ")
            menu()
            command = str(get_transaction())

    return balance


def menu():
    print('1 - Пополнить\n2 - Снять\n3 - Просмотреть баланс\n4 - Выйти')


def get_transaction():
    transaction = str(input("Выберите операцию: "))
    return transaction


def format_currency(amount):
    return f'{amount:_.2f}'


# пополнение баланса
def replenishment(amount):
    global balance
    global count

    count += 1

    if amount % 50 == 0:
        balance = balance + amount
        return balance

    else:
        print('Сумма пополнения должна быть кратна 50')


# снятие наличных
def withdrawal(amount):
    global balance
    global count

    count += 1

    if balance > 0:
        if amount % 50 == 0 and amount > 0:
            percent = ((amount * percent_withdrawal) / 100)
            if percent < 30:
                percent = 30
                balance = balance - amount - percent
                print(f'Будет списано: {amount + percent}')

            elif percent > 600:
                percent = 600
                balance = balance - amount - percent
                print(f'Будет списано: {amount + percent}')

            else:
                balance = balance - amount - percent
                print(f'Будет списано: {amount + percent}')

        else:
            print('Сумма снятия должна быть кратна 50')

    else:
        print(f'Не достаточно средств для операции\nУ вас на счету{balance}')

    return balance


if __name__ == "__main__":
    program()
