import random
count = int(input())

def randomList(count):
    print(random.sample(range(1, 10), count))
    return

print(randomList(count))