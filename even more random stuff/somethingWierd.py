def search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        s = (l + r) // 2
        if arr[s]:
            return s
        elif x > arr:
            l = s + 1
        else:
            r = s - 1
        return -1


a = 20
tab = [1, 2, 3, 4]
result = search(tab, a)
print(result)
