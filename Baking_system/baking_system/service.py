from Baking_system.baking_system.models import UserData


class Bill:
    def __init__(self, person: UserData, score: int = 0,) -> None:
        self.score = score
        self.person = person
        self.history = []
        self.add_summ = 0
        self.whithdraw_summ = 0

    def add_score(self, summ: float) -> float:
        self.add_summ = summ
        self.score += summ
        self.add_history()
        return self.score

    def whithdraw_money(self, summ: float) -> float:
        self.whithdraw_summ = summ
        self.score -= summ
        self.add_history()
        return self.score

    def add_history(self):
        _dict = {
            "user": self.person.user.get("login"),
            "add_summ": self.add_summ,
            "withdraw_money": self.whithdraw_summ,
            "score": self.score
        }
        self.history.append(_dict)

    def view_score(self) -> None:
        print(self.score)
