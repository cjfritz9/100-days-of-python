from turtle import Turtle, Screen, colormode
from random import randint, choice

screen = Screen()
screen.setup(500, 500)
screen.bgcolor('black')

donatello = Turtle()
colormode(255)

donatello.penup()
donatello.setpos(-120, 60)
donatello.pendown()
donatello.speed(0)
donatello.shape("turtle")
donatello.pensize(10)

sides = 3

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)

  return (r, g, b)

for _ in range(250):
  angle = randint(0, 3) * 90
  donatello.color(random_color())
  donatello.right(angle)
  donatello.forward(50)


screen.exitonclick()



