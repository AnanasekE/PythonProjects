import turtle
import time


turtle.speed(-1)
turtle.Screen().setup(600, 600)




def line(length):
    turtle.fd(length)
    turtle.left(60)
    turtle.fd(length)
    turtle.right(120)
    turtle.fd(length)
    turtle.left(60)
    turtle.fd(length)
    turtle.right(30)
    if length < 1:
        return
    print(length)
    return line(length * 0.99)


print(line(20))


time.sleep(1)

turtle.done()
