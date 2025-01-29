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
