print("Добро пожаловать в банковскую систему!")

class UserData:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.user = {
            "login" : self.login ,
            "pasword" : self.password
        }
        print(f"Пользователь {self.login} зарегистрироан!")


class Authorization:

    def __init__(self, person: UserData):
        self.person = person

    def is_login(self ,auth_login, auth_password ):
        self.auth_login = auth_login
        self.auth_password = auth_password

        if self.person.user.get("login") == auth_login and self.person.user.get("pasword") == auth_password:
            print("Аторизация успешна!")
        else:
            print("Пользователь не зарегистрирован!")

class Bill:
    def __init__(self, score: int = 0) -> None:
        self.score = score

    def add_score(self, summ: float) -> float:
        self.summ = summ
        self.score += summ
        return self.score

    def withdraw_money(self, summ: float) -> float:
        self.summ = summ
        self.score -= summ
        return self.score

    def view_score(self) ->None:
        print(self.score)

    def info(self):
        pass
