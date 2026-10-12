import turtle

#ekran ayarları:

screen=turtle.Screen()
screen.bgcolor("#f0f0f0")
screen.title("ASLAN")

t = turtle.Turtle()
t.speed(5)
t.width(3)

def daire_ciz(x, y, yaricap, renk):
    t.penup()
    t.goto(x,y - yaricap)
    t.pendown()
    t.fillcolor(renk)
    t.begin_fill()
    t.circle(yaricap)
    t.end_fill()

#Yele

daire_ciz(0, 0, 130, "#e67e22")

#kulaklar

daire_ciz(-70, 70, 28, "#d35400")
daire_ciz(70, 70, 28, "#d35400")
daire_ciz(-70, 70, 16, "#f39c12")
daire_ciz(70, 70, 16, "#f39c12")

#yüz

daire_ciz(0, 0, 95, "#f1c40f")

#gözler

daire_ciz(-35, 25, 10, "#2c3e50")
daire_ciz(35, 25, 10, "#2c3e50")

#burun

t.penup()
t.goto(-18, 5)
t.pendown()
t.fillcolor("#c0392b")
t.begin_fill()
t.goto(18,5)
t.goto(0,-15)
t.goto(-18,5)
t.end_fill()

#ağız
t.penup()
t.goto(0,-15)
t.pendown()
t.setheading(-90)
t.fd(12)

#sol dudak

t.setheading(200)
t.circle(16,120)

#sağ dudak

t.penup()
t.goto(0,-27)
t.pendown()
t.setheading(-20)
t.circle(-16,120)


t.hideturtle()
screen.exitonclick()
turtle.done
