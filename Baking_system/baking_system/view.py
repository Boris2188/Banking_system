class UserInput:

    def action(self) -> int:
        self.action: int = int(input("Введите действие: "))
        return self.action

    def login(self) -> str:
        self.login: str = input("Ведите логин ")
        return self.login

    def password(self) -> str:
        self.password: str = input("Ведите пароль ")
        return self.password






