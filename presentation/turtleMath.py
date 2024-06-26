import turtle
import math

# Create line turtle
mathTurtle = turtle.Turtle()
mathTurtle.color("red")
mathTurtle.speed("fastest")

# Setup grid numbers
yAxis = turtle.Turtle()
yAxis.hideturtle()
yAxis.color("#767889")
yAxis.speed("fastest")

xAxis = turtle.Turtle()
xAxis.hideturtle()
xAxis.color("#767889")
xAxis.speed("fastest")

negyAxis = turtle.Turtle()
negyAxis.hideturtle()
negyAxis.color("#767889")
negyAxis.speed("fastest")

negxAxis = turtle.Turtle()
negxAxis.hideturtle()
negxAxis.color("#767889")
negxAxis.speed("fastest")

# Make grid
yAxis.lt(90)
negyAxis.rt(90)

negxAxis.lt(180)

mathTurtle.write("0")

for i in range(10):
    xAxis.forward(50)
    yAxis.forward(50)
    negxAxis.forward(50)
    negyAxis.forward(50)

    xAxis.write(f"{i + 1}")
    negxAxis.write(f"-{i + 1}")
    yAxis.write(f"{i + 1}")
    negyAxis.write(f"-{i + 1}")

# Funktion to display simple "y = a*x + b" graph
def displaySimpleGraph():

    mathTurtle.penup()

    print("Please provide simple function: y = ax + b")
    a = int(input("a = "))
    b = int(input("b = "))

    turnTurtle = 0
    if a > 0 or a < 0:
        for i in range(1, abs(a)):
            turnTurtle += 90 / math.pow(2, i)

        if a < 0:
            turnTurtle *= -1

        mathTurtle.lt(turnTurtle)

    mathTurtle.sety(b * 50)

    mathTurtle.pendown()

    mathTurtle.back(1000)
    mathTurtle.forward(2000)

# Run function
displaySimpleGraph()

# Keep turtle around
turtle.done()