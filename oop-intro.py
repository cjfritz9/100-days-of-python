# from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()

# timmy.color("green")
# timmy.shape("turtle")
# timmy.forward(100)

# screen.setup(720, 720)
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "c", "m");
table.add_column("Type", ["Electric", "Water", "Fire"], "c", "m");

print(table)
