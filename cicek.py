import turtle
screen= turtle.Screen()
screen.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.pensize(3)
tess.speed(10)




def ciz(someturtle, someside,somesize,):
    angle=360/someside
    for i in range(someside):
        someturtle.fd(somesize)
        someturtle.lt(angle)





#EX1

#tess.penup()
#tess.goto(0-50,-30)
#tess.pendown()
#tess.color("red")
#ciz(tess,8,100)
#screen.exitonclick()


#EX2

tess.color("red")
for i in range(20):
    ciz(tess,4,50,)
    tess.left(20)


tess.color("darkgreen")
tess.rt(127)
tess.fd(200)

tess.color("yellow")
tess.penup()
tess.goto(0,0)
tess.pendown()
tess.circle(6,90)

turtle.hideturtle()
screen.exitonclick()