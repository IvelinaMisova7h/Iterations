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
    def __init__(self, color, position):
        self.position = position
        self.color = color
        self.tur = turtle.Turtle()
        self.tur = shape("turtle")
        self.tur = color(color)
        self.tur.penup()
        self.tur.setpos(position)
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
    for color in colors:
        file_1.write(color + '0 \n')
    file_1.close()


def start_game_1():
