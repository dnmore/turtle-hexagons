from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.bgcolor('black')
hexagon = Turtle()
hexagon.speed('fastest')
colors = ['aquamarine', 'blue', 'chocolate', 'coral', 'cyan', 'DarkBlue', 'DarkGoldenrod', 'DarkOrchid1', 'DarkSalmon',
          'DeepPink', 'DeepSkyBlue']

num_sides = 6
side_length = 70
angle = 360 / num_sides


def create_hexagons(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        hexagon.setheading(hexagon.heading() + size_of_gap)
        for i in range(num_sides):
            hexagon.color(choice(colors))
            hexagon.forward(side_length)
            hexagon.right(angle)


create_hexagons(5)
hexagon.hideturtle()
screen.exitonclick()
