from turtle import *
import math
import random
import turtle

window_width = 500
window_height = 500

turtles = 8

turtle.screensize(window_width, window_height)


class racer(object):
    # initialize constructor
    def __init__(self, color_1, position_1):
        self.position = position_1
        self.color = color_1
        self.tur = turtle.Turtle()
        self.tur = shape("turtle")
        self.tur = color_1(color_1)
        self.tur.penup()
        self.tur.setpos(position_1)
        self.tur.setheading(90)

    def move_1(self):
        rand = random.randrange(1, 20)
        self.position = (self.position[0], self.position[1] + rand)
        self.tur.penup()
        self.tur.forward(rand)

    def reset_1(self):
        self.tur.penup()
        self.tur.setposition(self.position)


def set_up_file(name, colors):
    file_1 = open(name, 'w')
    for color_2 in colors:
        file_1.write(color_2 + '0 \n')
    file_1.close()


def start_game_1():
    t_list = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["yellow", "blue", "green", 'cyan', 'red', 'purple', 'pink', 'brown', 'black']
    start = -(window_width / 2) + 20
    for t in range(turtles):
        new_position_x = start + t * window_width // turtles
        t_list.append(racer(colors[t], (new_position_x, -230)))
        t_list[t].tur.showturtle()

    run = True
    while run:
        for t in t_list:
            t.move_1()

        max_color = []
        max_dis = 0
