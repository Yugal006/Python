import turtle

colors = ['red','yellow','green','purple','blue','white']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)

for i in range(250):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)

t.hideturtle()
