import time
from turtle import Turtle, Screen
import random

from Food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.title("Snake Game")
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)

snake= Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.snakes[0].distance(food) < 20:
        food.change_pos()
        score.increase()
        snake.increase_snake()
    if snake.snakes[0].xcor() > 420 or snake.snakes[0].xcor() < -420 or snake.snakes[0].ycor() > 420 or snake.snakes[0].ycor() < -420:
        score.game_over()
        game_on = False

    for i in range(1, len(snake.snakes)):
        if snake.snakes[0].distance(snake.snakes[i]) < 10:
            score.game_over()
            game_on = False




screen.exitonclick()
