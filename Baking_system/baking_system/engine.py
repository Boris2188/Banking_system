from Baking_system.baking_system.view import UserInput
from Baking_system.baking_system.models import UserData, Authorization
from Baking_system.baking_system.service import Bill

login = None
password = None

user = UserData()
view = UserInput()
bill = Bill(user)

def start():

    print(view.welcome())
    print(view.start_info())
    action = view.action()

    while True:
        if action == 1:
            user = UserData(view.login(), view.password())
            auth = Authorization(user)
            login = auth.get_login()
            password = auth.get_password()
            action = view.action()
            continue
        elif action == 2:
            if view.login() == login and view.password() == password:
                print("авторизация успешна!!\n")
                dop_servis()
                break
            else:
                print("Неверный логин или пароль!")

        else:
            print("досвидания !!!")
            break


def dop_servis():

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
