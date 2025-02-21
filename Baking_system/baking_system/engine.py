from Baking_system.baking_system.view import UserInput
from Baking_system.baking_system.models import UserData, Authorization
from Baking_system.baking_system.service import Bill



user = UserData()
view = UserInput()


def start():
    login = None
    password = None

    print(view.welcome())
    print(view.start_info())

    while True:
        action = view.action()
        if login is None and action == 1:
            user = UserData(view.login(), view.password())
            auth = Authorization(user)
            login = auth.get_login()
            password = auth.get_password()
            print(f"Пользователь зарегистрирован!\n")
            print(f"1. Авторизация\n2. Выход\nВыберите действие: 1\n")
            continue
        elif login is not None and action == 1:
            if view.login() == login and view.password() == password:
                print("Добропожаловать !\n")
                dop_servis(user)

            else:
                print("Неверный логин или пароль!")
                break

        else:
            print("досвидания !!!")
            break


def dop_servis(user):
    bill = Bill(user)

    print(f"1. Пополнить счет\n2. Вывести средства\n3. Просмотреть баланс\n"
          f"4. Просмотреть историю операций\n5. Выход")

    while True:
        action = view.action()
        if action == 1:
            sum = view.add_money()
            a = bill.add_score(sum)
            print(a)
            continue
        elif action == 2:
            summ = view.whidthdraw_many()
            b = bill.whithdraw_money(summ)
            print(b)

        elif action == 3:
            bill.view_score()
            continue

        elif action == 4:
            c = bill.history
            print(c)

        else:
            print("Досвидания!!!")
