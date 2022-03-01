arr = []


def merge(str1, str2):
    if len(str1) > len(str2):
        smallest = str2
    else:
        smallest = str1

    for i in range(0, len(smallest)):
        arr.append(str1[i])
        arr.append(str2[i])

    return arr


print(merge('amogus', 'kot'))
