from turtle import Turtle
import random

class Food(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.75, 0.75)
    self.color("blue")
    self.speed("fastest")
    self.respawn()


  def respawn(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 260)
    self.goto(random_x, random_y)