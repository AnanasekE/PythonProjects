count = int(input())

tab = []
list1 = []

for j in range(count + 1):
    x = input().split(' ')
    tab.append(x)

print(tab)
print(tab[1][1])


def IncersionSorting(arr):
    for i in range(1, len(arr)):
        checked = arr[i]
        j = i - 1
        while j >= 0 and checked < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = checked
    # print(arr)
    return arr


if tab[-1][0] == '1':
    for j in range(len(tab) - 1):
        # debug
        # print(tab[j][1])
        list1.append(tab[j][1])
    IncersionSorting(list1)
if tab[-1][0] == '0':
    for j in range(len(tab) - 1):
        # debug
        # print(tab[j][0])
        list1.append(tab[j][0])
    # IncersionSorting(list1)

print(list1)

