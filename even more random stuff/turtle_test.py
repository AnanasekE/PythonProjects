import turtle
import sys
from time import sleep


def settings():
    turtle.bgcolor("black")
    turtle.color("white")
settings()


def exit_out():
    sleep(3)
    sys.exit(0)


def square(a):
    for i in range(4):
        turtle.fd(a)
        turtle.rt(90)


def definedSquare():
    for i in range(4):
        turtle.forward(150)
        turtle.right(90)


def undefinedSquare():
    a = int(input("Enter :"))
    for i in range(4):
        turtle.fd(a)
        turtle.right(90)


def triangle():
    # a = int(input("Enter: "))
    a = 100
    for i in range(3):
        turtle.fd(a)
        turtle.rt(120)


def ThreeSquares():
    # a = int(input("Enter: "))
    a = 100
    for i in range(3):
        square(a)
        turtle.up()
        turtle.fd(a)
        turtle.down()


def infiniteSquares():
    # a = int(input("Enter: "))
    a = 100  # input
    count = 4  # input
    for i in range(count):
        square(a)
        turtle.up()
        turtle.fd(a)
        turtle.down()


# insert function here ↓
triangle()

# end here
exit_out()