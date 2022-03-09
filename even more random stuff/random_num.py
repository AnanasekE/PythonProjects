import random
x = int(input("set x: "))
y = int(input("set y: "))
z = int(input("set z: "))
w = int(input("set w: "))
a = random.randrange(x,y)
b = random.randrange(z,w)
c = a + b
print(c)