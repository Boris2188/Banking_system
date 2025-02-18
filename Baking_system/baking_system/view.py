class UserInput:

    def action(self) -> int:
        action = int(input("Введите действие :"))
        return action

    def login(self) -> str:
        login = input("Ведите логин ")
        return login

    def password(self) -> str:
        password = input("Ведите пароль ")
        return password

    def welcome(self):
        return f"Добро пожаловать в банковскую систему!\n"

    def start_info(self):
        return f"1. Регистрация\n2. Авторизация\n3. Выход\nВыберите действие: 1"

    def add_money(self):
        sum = int(input("Какую вы сумму хотите внести: "))
        return sum

    def whidthdraw_many(self):
        sum = int(input("Какую вы сумму хотите вывести: "))
        return sum

    def se_action(self):
        print(f"1. Пополнить счет\n2. Вывести средства\n3. "
              f"Просмотреть баланс\n"
               f"4. Просмотреть историю операций\n5. Выход")
