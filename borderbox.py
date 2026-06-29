from turtle import Turtle

class BorderBox(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.color("white")
        self.pendown()
        self.forward(555)
        self.right(90)
        self.forward(550)
        self.right(90)
        self.forward(555)
        self.right(90)
        self.forward(550)