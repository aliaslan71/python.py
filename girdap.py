import turtle

t=turtle.Turtle()
renkler = ["red","green","blue","yellow","orange","purple","pink","brown","gray","cyan" ]
turtle.bgcolor("black")

for i in range(220):
    renk_sirasi=(i % 10)
    t.pensize(3)
    t.color("red")
    t.speed(10)
    t.fd( i * 1)
    t.right(59)


turtle.exitonclick()
turtle.done()