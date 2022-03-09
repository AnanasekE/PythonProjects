x = 10
list1 = list(())
while True:
    result = x % 2
    x /= 2
    list1.append(result)
    print(x)
    if x == 1 or x == 0:
        list1.append(1)
        break

print(list1)

