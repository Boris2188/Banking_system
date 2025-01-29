class UserData:

    def __init__(self, login, password):
        self.user = {
            "login": login,
            "pasword": password
        }


class Authorization:

    def __init__(self, person: UserData):
        self.person = person

    def is_login(self, auth_login, auth_password):
        self.auth_login = auth_login
        self.auth_password = auth_password

        if (self.person.user.get("login") == auth_login and
                self.person.user.get("pasword") == auth_password):
            print("Аторизация успешна!")
        else:
            print("Пользователь не зарегистрирован!")
