tab = [1, 34, 52, 43, 100, 58, 82, 64]



def test(arr):
    potMin = []
    potMax = []
    for i in range(0, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            potMax.append(arr[i])
            potMin.append(arr[i + 1])
        else:
            potMax.append(arr[i + 1])
            potMin.append(arr[i])
    if len(arr) % 2 == 1:
        potMax.append(arr[-1])
        potMin.append(arr[-1])
    print(potMin,potMax)
    
    min = potMax[0]
    max = potMin[0]

    for n in range(potMin[0], len(potMin)):
        if min > potMin[n]:
            min = potMin[n]
        if max < potMax[n]:
            max = potMax[n]

    return min,max



print(test(tab))