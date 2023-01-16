# This is a sample Python script.
# import turtle
# from turtle import Turtle,Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# print(timmy)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
pt=PrettyTable()
pt.align="l"
pt.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
pt.add_column("Type",["Electric","Water","Fire"])
print(pt)