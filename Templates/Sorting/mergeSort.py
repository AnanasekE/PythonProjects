arr = [9, 7, 1, 2, 5, 4, 3, 2]
list1 = []


# def merge(arr, left, right):
#     for i in range(0, len(left)):
#         print('merge[i]:', i)
#         if left[i] == right[i]:
#             list1.append(left[i])
#         elif left[i] > right[i] :
#             list1.append(right[i])
#             list1.append(left[i])
#         else:
#             list1.append(left[i])
#             list1.append(right[i])
#         print('list1',i,list1)

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


print(mergeSort(arr))