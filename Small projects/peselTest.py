def peselCheck(count, pesel):
    count = 1
    strPesel = []
    arr2 = []
    check = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    for i in range(0, count):
        pesel = "12345678901"
        if len(pesel) == 11:
            for j in pesel:
                strPesel.append(j) #pesel jako string
                for k in strPesel:
                    print(k)



        print(strPesel)


print(peselCheck(1, 1))
