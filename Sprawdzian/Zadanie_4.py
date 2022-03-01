import math


def sito(num):
    if num < 2:  # stops you if num is less than 2
        print('You can`t do that!')
        return

    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False
    for i in range(2, int(math.sqrt(num) + 1)):
        if arr[i]:
            for j in range(i * i, num + 1, i):
                arr[j] = False

    print([i for i, val in enumerate(arr) if val])
    return arr


max = 256
text = str(input("Input your text: "))

for i in text:
    szukana = ord(i)
    if szukana < max:
        max = szukana

print(sito(szukana))
