from Baking_system.baking_system.view import UserInput
from Baking_system.baking_system.models import UserData,Authorization
from Baking_system.baking_system.service import  Bill

def main():
    action = 0
    corect = None
    print("1. Регистрация \n2. Авторизация \n3. Выход\n"
          "Выберите действие: 1 если Вы не зарегистрированы!")
    user = UserData()
    action = 0
    while True:
       try:
           action = UserInput.action(user)
           if action <= 0 >3:
               print("число от 1 до 3")
               break
       except ValueError:
           print("Это не целое число. Попробуйте снова...")

    if action == 1:
        user = UserData(UserInput.login(user), UserInput.password((user)))
        print(f"Пользователь {Authorization(user).get_login()}  успешно зарегестрирован!\n")
        print("1. Авторизация\n2. Выход\nВыберите действие: 2")
    action = UserInput.action(user)
    if action == 2:
        corect = Authorization(user).is_login(UserInput.login(user), UserInput.password(user))
        if corect == True:
            print("Авторизация успешна!")
        else:
            print("Пробуйте заново")





if __name__ == "__main__":
    print("Добро пожаловать в банковскую систему!\n")
    main()




