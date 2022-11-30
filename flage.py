import  turtle
t = turtle.Pen()
t.right(-90)
for i in range(10):
    for colours in ["red","magenta","blue","cyan","green","yellow","white","black"]:
        t.color(colours)
        t.speed(0)
        t.shape("turtle")
        t.right(i)
        
t.color("black","white")
t.right(90)
t.pensize(3)
t.up()
t.goto(0,-250)
t.pd()
t.right(180)
t.speed(5)
#base
t.begin_fill()
t.fillcolor("#6E2C00")
t.fd(100)
t.left(90)
t.fd(30)
t.left(90)
t.fd(200)
t.left(90)
t.fd(30)
t.end_fill()
t.left(90)
t.fd(150)
t.begin_fill()
t.fillcolor("#A04000")
t.right(90)
t.fd(30)
t.right(90)
t.fd(100)
t.right(90)
t.fd(30)
t.end_fill()

#-------*--------

#pole of flage
t.up()
t.goto(0,-220)
t.pd()
t.right(180)
t.fd(500)
t.pensize(3)
t.up()
t.goto(10,290)
t.pd()
t.begin_fill()
t.fillcolor("#424242")
t.pensize(3)
t.circle(10)
t.end_fill()
t.up()
t.goto(0,230)
t.pd()

#-----------*--------------

#flage

t.right(90)
t.begin_fill()
t.fillcolor("orange")
t.fd(200)
t.right(90)
t.fd(50)
t.right(90)
t.fd(200)
t.end_fill()
t.bk(200)
t.right(-90)
t.begin_fill()
t.fillcolor("white")
t.fd(50)
t.right(90)
t.fd(200)
t.right(90)
t.fd(50)
t.end_fill()
t.bk(100)
t.right(90)
t.begin_fill()
t.fillcolor("green")
t.fd(200)
t.left(90)
t.fd(50)
t.left(90)
t.fd(200)
t.end_fill()
t.right(90)
t.fd(50)
t.right(90)
t.fd(200)
t.bk(200)
t.left(90)
t.fd(50)
t.bk(150)

#ashok chakra
t.up()
t.fd(75)
t.right(90)
t.fd(125)
t.pd()
t.pencolor("navy")
t.left(90)
t.circle(25)
t.left(90)
t.pensize(2)
t.fd(50)
t.bk(25)
t.right(90)
t.fd(25)
t.bk(50)
t.fd(25)
t.right(45)
t.fd(25)
t.bk(50)
t.fd(25)
t.right(90)
t.fd(25)
t.bk(50)
t.fd(25)

for i in range(29):
    t.shape("classic")
    t.right(15)
    t.fd(25)
    t.bk(50)
    t.fd(25)
    
t.right(15)
t.bk(9)
t.right(98)
t.pensize(9)
t.circle(8)
t.up()
t.shape("turtle")
t.right(90)
t.pensize(3)
t.goto(0,200)
t.right(-45)
t.left(8)
t.fd(78)
t.pensize(3)
t.pd()
t.right(90)
t.circle(-180,180) 
t.circle(50,195)
t.circle(-20,140)
t.circle(-10,150)
t.up()
t.goto(-100,200)
t.right(-94)
t.fd(100)
t.right(45)
t.pd()
t.speed(10)
t.pensize(6)
t.pencolor("#5319FB")
t.bk(40)
t.right(90)
t.pencolor("#BC00FE")
t.fd(40)
t.bk(80)
t.right(45)
t.right(90)
t.pencolor("#1B02A3")
t.circle(10,180)
t.pencolor("#006AF9")
t.circle(-10,180)
t.pencolor("#00C0F9")
t.circle(10,180)
t.pencolor("#DC00FE")
t.circle(-10,180)
t.pencolor("#BC00FE")
t.fd(10)
t.pencolor("#5319FB")
t.fd(10)
t.up()
t.fd(100)
t.pd()
    
t.hideturtle()