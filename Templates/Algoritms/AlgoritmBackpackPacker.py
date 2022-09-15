cena = [8, 3, 5]
weight = [5, 3, 4]
name = ['Pick', 'Potato', 'BMW']
backpack = 8
best = []
arr = [[5, 8, 'Pick'], [3, 3, 'Potato'], [5, 4, 'BMW']]
# for g in range(len(cena)):
#     best.append(cena[g]/weight[g])

arr.sort(key=lambda x: x[1] / x[0])
arr.reverse()
print(arr)

# best, name = (list(t) for t in zip(*sorted(zip(best, name))))
# best.reverse()
# name.reverse()
# print(best)
# print(name)
