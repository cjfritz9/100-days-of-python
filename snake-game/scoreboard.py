from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.goto(0, 260)
    self.color("white")
    self.update()
    self.hideturtle()

  def update(self):
    self.clear()
    self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

  def increase_score(self):
    self.score += 1
    self.update()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", False, ALIGNMENT, FONT)