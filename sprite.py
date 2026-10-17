import turtle
screen = turtle.Screen()
tess=turtle.Turtle()

screen.bgcolor("green")
tess.color("blue")

def drawSprite(someturtle,legs,lenght):
    angle=360/legs
    for i in range(legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)

drawSprite(tess,5,100)
screen.exitonclick()