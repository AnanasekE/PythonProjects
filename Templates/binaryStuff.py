# number = int(input())
# binary = ""
# while number > 0:
#     if number % 2 == 0:
#         binary += "0"
#     else:
#         binary += "1"
#     number //= 2
# binary = binary[ : :-1]
# print(binary)


def binary_search(arr, szukana):
    right = 0
    left = len(arr) - 1
    center = 0

    while right <= left:
        center = (left + right) // 2

        if arr[center] < szukana:
            right = center + 1

        elif arr[center] > szukana:
            left = center - 1

        else:
            return center

    return -1



arr = [2, 3, 4, 10, 40]
szukana = 10


print(binary_search(arr, szukana))