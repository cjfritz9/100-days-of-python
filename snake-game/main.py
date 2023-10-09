from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.respawn()
    snake.add_segment()
    scoreboard.increase_score()
  
  if snake.boundary_collision():
    game_is_on = False
    scoreboard.game_over()

  for segment in snake.segments[2:]:
    if snake.head.distance(segment) < 15:
      game_is_on = False
      scoreboard.game_over()





screen.exitonclick()