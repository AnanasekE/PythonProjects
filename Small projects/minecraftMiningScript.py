import pyautogui as pag
import keyboard
import pynput
import time


# mouse = pynput.mouse.Controller()
# mouse.move(10, 10)


# wh = pag.size()
# print(wh)


def square3x3():
    pag.leftClick()
    pag.move(100, 0, 0)
    pag.leftClick()
    pag.move(0, 100, 0)
    pag.leftClick()
    pag.move(-100, 0, 0)
    pag.leftClick()
    pag.move(-100, 0, 0)
    pag.leftClick()
    pag.move(0, -100, 0)
    pag.leftClick()
    pag.move(0, -100, 0)
    pag.leftClick()
    pag.move(100, 0, 0)
    pag.leftClick()
    pag.move(100, 0, 0)
    pag.leftClick()
    pag.move(-100, 100, 0)


def moose2():
    while True:
        try:
            if keyboard.is_pressed('p'):
                for i in range(100):
                    square3x3()
                    keyboard.press('w')
                    time.sleep(0.2)
                    keyboard.release('w')
                    if keyboard.is_pressed('o'):
                        break
            if keyboard.is_pressed('o'):
                break

        except:
            continue


# def moose():
#     # mouse = Controller()
#
#     mouse.position = (100, 200)
#     mouse.move(200, -100)


# def move_smooth(xm, ym, t):
#     for i in range(t):
#         if i < t / 2:
#             h = i
#         else:
#             h = t - i
#         mouse.move(h * xm, h * ym)
#         time.sleep(1 / 60)


moose2()

# while True:
#     if keyboard.is_pressed('p'):
#         move_smooth(2, 2, 40)
#     if keyboard.is_pressed('o'):
#         break
