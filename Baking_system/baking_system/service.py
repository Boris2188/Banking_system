from Baking_system.baking_system.models import UserData

class Bill:
    def __init__(self, person: UserData, score: int = 0,) -> None:
        self.score = score
        self.person = person
        self.history = []

    def add_score(self, summ: float) -> float:
        self.score += summ
        return self.score

    def withdraw_money(self, summ: float) -> float:
        self.score -= summ
        self.add_history(self.score)
        return self.score

    def add_history(self, summ):
        _dict = {
            "user": self.person.user.get("login"),
            "summ": summ,
            "score": self.score
        }
        self.history.append(_dict)

    def view_score(self) -> None:
        print(self.score)
