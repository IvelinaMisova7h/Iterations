from turtle import *
from random import randint  # Generating random values

speed(0)  # Give the speed to the turtle and 0 is the fastest speed.
penup()  # Move turtle without leaving tracks
goto(-140, 140)  # Move turtle to the position

for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)  # Function is used to move the turtle in the forward direction
        pendown()  # The default state of turtle. Function is mostly useful to reestablish pendown state
        # after using .penup()
        forward(10)
    penup()
    backward(160)  # Function is used to move the turtle in the backward direction
    left(90)  # Function is used to move the turtle in the left direction
    forward(20)

tur1 = Turtle()
tur1.color('green')  # Give the green color to the turtle
tur1.shape('turtle')  # Give the shape to the turtle

tur1.penup()
tur1.goto(-160, 100)
tur1.pendown()

for turn in range(10):
    tur1.right(36)

tur2 = Turtle()
tur2.color('red')
tur2.shape('turtle')

tur2.penup()
tur2.goto(-160, 70)
tur2.pendown()

for turn in range(72):
    tur2.left(5)

tur3 = Turtle()
tur3.shape('turtle')
tur3.color('brown')

tur3.penup()
tur3.goto(-160, 40)
tur3.pendown()

for turn in range(60):
    tur3.right(6)

tur4 = Turtle()
tur4.shape('turtle')
tur4.color('orange')

tur4.penup()
tur4.goto(-160, 10)
tur4.pendown()

for turn in range(30):
    tur4.left(12)

for turn in range(100):
    tur1.forward(randint(1, 5))  # Move forward with a random number of steps
    tur2.forward(randint(1, 5))
    tur3.forward(randint(1, 5))
    tur4.forward(randint(1, 5))
