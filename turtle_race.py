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
