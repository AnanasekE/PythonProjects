arr1 = [4, 2, 7, 1, 3]


def IncersionSorting(arr):
    for i in range(1, len(arr)):
        checked = arr[i]
        j = i-1
        while j >= 0 and checked < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j + 1] = checked
    print(arr)
IncersionSorting(arr1)

# pętla for od 1 do len(arr)
# zapamiętujemy i
# index  od którego porównamy
# while i >=0 and i > arr[j]
# set j = j+1
# zmniejszyć j
# na index j+1 wstawić arr[i]




# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     print(arr)

