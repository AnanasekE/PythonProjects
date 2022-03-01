x = int(input())
for i in range(0,26,x):
    print(chr(ord('a')+i),end=' ')
    print(chr(ord('A')+i),end=' ')