

def recursiveSum(a, b):
    if a == 0:
        return b
    else:
        return recursiveSum(a - 1, b + 1)


recursiveSum(3, 2)
print()

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

# print(factorial(997))'



def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)


for i in range(0,100):
    print(i,fibonacci(i))