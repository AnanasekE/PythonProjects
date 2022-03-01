arr = []
for i in range(-10000 + 1, 10000 + 1):
    arr.append(i)


def binary_search(arr, x):
    right = 0
    left = len(arr) - 1
    center = 0

    while right <= left:
        center = (left + right) // 2

        if arr[center] < x:
            right = center + 1

        elif arr[center] > x:
            left = center - 1

        else:
            return center

    return -1

x = int(input("Input your number: "))

print(binary_search(arr, x))