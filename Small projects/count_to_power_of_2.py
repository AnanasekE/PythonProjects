import time
print("Select amount of times to count to a power of 2")
x = int(input("select x: "))
i = 0
count = 1
if x < 99999:
    while i < x:
      count = count + count
      time.sleep(0.5)
      i = i + 1
      print (count)
else:
        print("Select a lower number")

time.sleep(1)
print("Final count: ",count)