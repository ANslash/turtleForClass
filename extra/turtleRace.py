import turtle
from time import sleep
import random

#   creating field
field = turtle.Turtle()
field.hideturtle()
field.speed(0)
field.penup()
field.setposition(-350, 160)
field.write("Start")
field.seth(-90)
field.forward(10)
field.pendown()
field.forward(150)
field.penup()
field.setposition(350, 160)
field.write("End")
field.forward(10)
field.pendown()
field.forward(150)
field.penup()
field.setposition(0, 200)

#   Setting up racers turtles
t0 = turtle.Turtle()
t0.color("red")
t0.penup()
t0.setposition(-350, 150)

t1 = turtle.Turtle()
t1.color("blue")
t1.penup()
t1.setposition(-350, 100)

t2 = turtle.Turtle()
t2.color("green")
t2.penup()
t2.setposition(-350, 50)

t3 = turtle.Turtle()
t3.color("orange")
t3.penup()
t3.setposition(-350, 0)

racers = [t0, t1, t2, t3]

while t0.xcor() <= 350 and t1.xcor() <= 350 and t2.xcor() <= 350 and t3.xcor() <= 350:
    t0.forward(random.randint(0,20))
    t1.forward(random.randint(0,20))
    t2.forward(random.randint(0,20))
    t3.forward(random.randint(0,20))
    sleep(0.1)

field.write("WE HAVE A WINNER!!!")

turtle.done()