path = '/home/janek/Downloads/exercise1_przyklad.txt'
# path = input()

with open(path, 'r') as f:
    data = f.read()

data = data.strip().split()
data = [a.split(',') for a in data]
data = [list(map(int, a)) for a in data]

for i in range(len(data)):
    data[i].sort()

    if data[i][0] == 0:
        data[i][0], data[i][1] = data[i][1], data[i][0]

    print(data[i])

# TODO less time
