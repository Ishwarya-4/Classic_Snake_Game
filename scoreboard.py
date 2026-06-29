from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.file = open("score.txt", "r")
        self.highscore = int(self.file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.display_score()
        self.file.close()

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score}                       High Score = {self.highscore}", align="center", font=('Calibri', 14, 'bold'))

    def increase_score(self):
        self.score += 1
        self.display_score()

    def score_reset(self):

        if self.score > self.highscore:
            with open("score.txt", "w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER 😵", align="center", font=('Courier', 18, 'bold'))
