import random


def randomList(count):
    arr = random.sample(range(1, 15), count)
    return arr


def bubbleSort(arr):
    print("unsorted array:", arr)
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    print("sorted array:  ", arr)


bubbleSort(randomList(5))
