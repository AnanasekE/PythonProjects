import turtle
import time


turtle.speed(-1)
turtle.Screen().setup(600, 600)




def line(length):
    for i in range(12):
        turtle.fd(length)
        turtle.left(60)
        turtle.fd(length)
        turtle.right(120)
        turtle.fd(length)
        turtle.left(60)
        turtle.fd(length)
        turtle.right(30)

def saw(length):
    turtle.shape('turtle')
    for i in range(12):
        turtle.fd(length)
        turtle.left(60)
        turtle.fd(length)
        turtle.right(120)
        turtle.fd(length)
        turtle.right(30)
        turtle.fd(length)
        turtle.left(60)
        # turtle.home()

    turtle.circle(50)

saw(20)
# line(20)

time.sleep(1)

turtle.done()

