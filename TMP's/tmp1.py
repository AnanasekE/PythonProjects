# def's
list1 = []


def merge(arr, left, right):
    i = 0
    ip = 0
    il = 0

    while il < len(left) and ip < len(right):
        if il < ip:
            arr[i] = il
            il += 1
        else:
            arr[i] = ip
            ip += 1
        i += 1
    while il < len(left):
        if il < ip:
            arr[i] = il
            il += 1
        else:
            arr[i] = ip
            ip += 1
        i += 1
    while ip < len(right):
        if ip < il:
            arr[i] = ip
            ip += 1
        else:
            arr[i] = il
            il += 1
        i += 1


def mergeSort(arr):
    if len(arr) > 1:
        arrCenter = len(arr) // 2
        left = arr[:arrCenter]
        right = arr[arrCenter:]
        mergeSort(left)
        # print('left:', left)
        mergeSort(right)
        # print('right:', right)
        merge(arr, left, right)
        return arr


# wczytywanie imienia, nazwiska i oceny
cls = int(input())
state = True
for i in range(cls):
    arr = []
    state = True
    while state:
        personInput = input()
        if personInput == '-':
            state = False
        personInput = personInput.split()

        arr.append(personInput)
        if arr[-1][0] == '-':
            arr.pop(-1)


#
    mergeSort(arr)




#
