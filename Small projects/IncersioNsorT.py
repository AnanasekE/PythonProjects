count = int(input())

tab = []
list1 = []

for j in range(count + 1):
    x = input().split(' ')
    if x[0] == '0' or '1':
        pass
    else:
        x[1] = int(x[1])
    tab.append(x)

print(tab)



def IncersionSorting(arr):
    mode = 0
    if arr[-1][0] == '1':
        mode = 1
    arr.pop(-1)
    for i in range(1, len(arr)):
        checked = arr[i]
        j = i - 1
        if mode == 0:
            while j >= 0 and checked[mode] < arr[j][mode]:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = checked

        else:
            while j >= 0 and checked[mode] > arr[j][mode]:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = checked
    # print(arr)
    return arr


IncersionSorting(tab)
print(tab)

for k in range(len(tab)):
    print(tab[k][0], tab[k][1])


