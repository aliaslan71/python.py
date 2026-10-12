import turtle
import math

wn=turtle.Screen()
wn.bgcolor("black")
alex=turtle.Turtle()
alex.speed(10)
alex.pencolor("red")
alex.pensize(4)

def heart(n):
    x=15 * math.sin(n) ** 3
    y=12 * math.cos(n) -5*\
    math.cos(2*n)- 2*\
    math.cos(3*n)-\
    math.cos(4*n)
    return x,y

for i in range (16):
    alex.pendown()
    for j in range(0,100):
        x,y = heart(j/15)
        alex.goto(x*i,y*i)



wn.exitonclick()