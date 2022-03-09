list1 = list()
while True:
    x = input()
    if x == "end":
        for i in list1:
            if i %2 == 0:
                print("even")
            else:
                print("odd")
        break
    else:
        x = int(x)
        list1.append(x)