from Baking_system.baking_system.models import UserData

class UserInput:
    print("Добро пожаловать в банковскую систему!\n")
    print("1. Регистрация \n2. Авторизация \n3. Выход\n"
          "Выберите действие: 1 если Вы не зарегистрированы!\n")

    def __init__(self, option):
        self.option = option
        if self.option == 1:
            login = input("ведите логин ")
            password = input("Ведите пароль ")
            UserData(login, password)




a = UserInput(1)