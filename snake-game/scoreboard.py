from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

DB = "data.txt"

class Scoreboard(Turtle):

  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    with open(DB, "r") as hs:
      self.high_score = int(hs.read())
    self.goto(0, 260)
    self.color("white")
    self.update()
    self.hideturtle()

  def update(self):
    self.clear()
    self.write(f"Score: {self.score} - High Score: {self.high_score}", False, ALIGNMENT, FONT)

  def increase_score(self):
    self.score += 1
    self.update()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open(DB, "w") as hs:
        hs.write(str(self.high_score))
    self.score = 0;
    self.update()

  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("GAME OVER", False, ALIGNMENT, FONT)