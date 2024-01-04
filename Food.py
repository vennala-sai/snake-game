import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.setposition(random.randint(0, 280), random.randint(0,280))

    def change_pos(self):
        self.setposition(random.randint(0, 280), random.randint(0, 280))