import turtle
from time import sleep
from random import randrange
turtle.speed(1)
turtle.Screen().setup(600 + 4, 600 + 8)
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.up()
t1.goto(200, 100)
t1.down()
t1.right(90)
t1.fd(200)
t1.up()
t1.goto(0, 0)
t1.left(90)
t1.down()



def t1forward():
    t1.fd(50)
def t1right():
    t1.right(90)
def t1left():
    t1.left(90)
def t2forward():
    t2.fd(50)
def t2right():
    t2.right(90)
def t2left():
    t2.left(90)


turtle.onkey(t1forward, "Up")
turtle.onkey(t1right, "Right")
turtle.onkey(t1left, "Left")
turtle.onkey(t2forward, "w")
turtle.onkey(t2right, "d")
turtle.onkey(t2left, "a")
turtle.listen()
rand = randrange(0,255)
t1.color(rand, rand, rand)
while True:
    if t1.xcor() >= 200:
        turtle.Screen().bye()
        break
    if t2.xcor() >= 200:
        turtle.Screen().bye()
        break
    turtle.update()


turtle.mainloop()
turtle.done()
