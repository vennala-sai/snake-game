from turtle import Turtle

class Snake:

    def __init__(self, color="white"):
        self.color = color
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        self.increase_snake()
        self.increase_snake()
        self.increase_snake()

    def increase_snake(self):
        snake = Turtle()
        snake.color(self.color)
        snake.shape("square")
        snake.penup()
        if self.snakes:  # Check if there are already segments in the snake
            x, y = self.snakes[-1].pos()  # Position the new segment at the last segment's position
            snake.setposition(x, y)
        else:
            snake.setposition(-20 * len(self.snakes), 0)
        snake.speed("fastest")
        self.snakes.append(snake)

    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            (x, y) = self.snakes[i - 1].pos()
            self.snakes[i].goto(x, y)
        self.snakes[0].forward(20)


    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)
