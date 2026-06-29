from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from borderbox import BorderBox

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

border = BorderBox()
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 275 or snake.head.xcor() < -279 or snake.head.ycor() > 270 or snake.head.ycor() < -279:
        score.score_reset()
        snake.reset_snake()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.score_reset()
            snake.reset_snake()

screen.exitonclick()