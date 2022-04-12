year = int(input('year: '))
a = year % 19
b = year % 4
c = year % 7
d = (a * 19 + 24) % 30
e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
w = 22 + d + e

if w > 31:
    w -= 31
if (d == 29 and e == 6) or (d == 28 and e == 6):
    w -= 7

print(w, 'kwietnia')
