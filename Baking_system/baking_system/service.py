from Baking_system.baking_system.models import UserData

class Bill:
    def __init__(self, person: UserData, score: int = 0,) -> None:
        self.score = score
        self.person = person
        self.history = []

    def add_score(self, add_summ: float) -> float:
        self.add_summ = add_summ
        self.score += add_summ
        self.add_history()
        return self.score

    def withdraw_money(self, whithd_summ: float) -> float:
        self.whithd_summ = whithd_summ
        self.score -= whithd_summ
        self.add_history(self.score)
        return self.score

    def add_history(self, summ):
        _dict = {
            "user": self.person.user.get("login"),
            "add_summ": self.add_summ,
            "withdraw_money": self.whithd_summ,
            "score": self.score
        }
        self.history.append(_dict)

    def view_score(self) -> None:
        print(self.score)
