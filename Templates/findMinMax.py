arr = [3, 10, 20, 34, 102, -30, 56, 15, 73, 100]


def minmax(arr):
    if len(arr) == 0:
        min = None
        max = None
        return
    min = arr[0]
    max = arr[0]
    for i in arr:
        if min > i:
            min = i
            print(min)
        if max < i:
            max = i
            print(max)
    return min, max





wynik = minmax(arr)
print(wynik)
