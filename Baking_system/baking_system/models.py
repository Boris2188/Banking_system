class UserData:

    def __init__(self, login=None, password=None):
        self.user = {
            "login": login,
            "pasword": password
        }


class Authorization():
    def __init__(self, person: UserData):
        self.person = person

    def get_login(self):
        return self.person.user.get("login")

    def get_password(self):
        return self.person.user.get("password")

    def is_login(self, auth_login, auth_password):
        if (self.get_login() == auth_login and
                self.get_password() == auth_password):
            return True
        else:
            return False
