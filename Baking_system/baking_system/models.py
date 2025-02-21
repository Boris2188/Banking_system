class UserData:

    def __init__(self, login=None, password=None):
        self.user = {
            "login": login,
            "password": password
        }


class Authorization:
    def __init__(self, person: UserData):
        self.person = person

    def get_login(self):
        return self.person.user.get("login")

    def get_password(self):
        return self.person.user.get("password")

