from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.4,0.4)
        self.color('white')
        self.speed(0)
        self.generate_food()

    def generate_food(self):
        x = random.randint(-275,275)
        y = random.randint(-275,275)
        self.goto(x,y)