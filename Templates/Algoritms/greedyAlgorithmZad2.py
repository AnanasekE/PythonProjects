coins = [5, 3, 1]
money = int(input("Your Money: "))
change = []
i = 0

while money >= 0 and i < len(coins):
    # print(money, coins[i])
    if money >= coins[i]:
        change.append(coins[i])
        money -= coins[i]
    else:
        i += 1
print(len(change))
