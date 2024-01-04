from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", mode="r") as d:
            self.high_score = int(d.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setposition(0, 350)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Times New Roman", 20, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER.", align="center", font=("Times New Roman", 40, "normal"))
        self.max_score()

    def increase(self):
        self.score += 1
        self.score_write()

    def max_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
