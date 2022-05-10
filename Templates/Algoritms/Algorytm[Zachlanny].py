arr = [500, 200, 100, 50, 20, 10, 5, 2, 1]
change = []
money = int(input("Your Money: "))
i = 0

while money >= 0 and i < len(arr):
    print(money, arr[i])
    if money >= arr[i]:
        change.append(arr[i])
        money -= arr[i]
    else:
        i += 1
print(change)
