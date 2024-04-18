import turtle
import time

#   Initialize variables and constants
CIRCLE_RADIUS = 200
HOUR_ARM = CIRCLE_RADIUS * 0.4
MINUTES_ARM = CIRCLE_RADIUS * 0.8
SECOND_ARM = CIRCLE_RADIUS * 0.6

NOTCH_LENGTH = CIRCLE_RADIUS * 0.1
CLOCK_FRAME = CIRCLE_RADIUS + 10

HOUR_TIC = 360/12
SEC_AND_MIN_TIC = 360/60

HOUR_ROT = 12
MINUTES_ROT = 60
SECOND_ROT = 60

SET_TURTLE_UPWARDS = 90

#   Create hour turtle
h = turtle.Turtle()
h.hideturtle()
h.speed('fastest')
h.color("red")

#   Create minutes turtle
m = turtle.Turtle()
m.hideturtle()
m.speed('fastest')
m.color("blue")

#   create seconds turtle
s = turtle.Turtle()
s.hideturtle()
s.speed('fastest')
s.color("green")


#   Setup of clock frame
clock = turtle.Turtle()
clock.hideturtle()

cl = turtle.Turtle() #   Turtle for clone use
cl.hideturtle()

clock.speed('fastest')
clock.penup()

#   Create frame for the clock
clock.setpos(0, -CLOCK_FRAME)
clock.pendown()
clock.circle(CLOCK_FRAME)
clock.penup()
clock.home()
clock.setpos(0,-CIRCLE_RADIUS)
clock.pendown()

#   Start clock
for i in range(HOUR_ROT):   #   create clock frame with hour notches
    clock.circle(CIRCLE_RADIUS, HOUR_TIC)
    cl = clock.clone()   #   Clone clock turtle to make notch
    cl.seth((HOUR_TIC * (i + 1) + 90))
    cl.forward(NOTCH_LENGTH)

clock.penup()
clock.home()

#   Move hour hand
for hour in range(HOUR_ROT):
    h.seth(-(HOUR_TIC * hour - SET_TURTLE_UPWARDS))
    h.pendown()
    h.forward(HOUR_ARM)
    h.penup()
    h.home()

    #   Move minutes hand
    for minutes in range(MINUTES_ROT):
        m.seth(-(SEC_AND_MIN_TIC * minutes - SET_TURTLE_UPWARDS))
        m.pendown()
        m.forward(MINUTES_ARM)
        m.penup()
        m.home()

        #   Move seconds hand
        for seconds in range(SECOND_ROT):
            s.seth(-(SEC_AND_MIN_TIC * seconds - SET_TURTLE_UPWARDS))
            s.pendown()
            s.forward(SECOND_ARM)
            s.penup()
            s.home()
            time.sleep(.1)

            for i in range(5):  #   Undo to remove clone of seconds arm
                s.undo()

        for i in range(5):      #   Undo to remove clone of minutes arm
            m.undo()

for i in range(5):              #   Undo to remove clone of hours arm
    h.undo()
