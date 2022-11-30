import turtle

t = turtle.Turtle()
t.pensize(2)
turtle.bgcolor("black")
ask = str(input("Choose a color:\n"))
t.pencolor(ask)
t.speed(0)

for i in range(1000):
    t.circle(10 + i, 45)

t.hideturtle()
