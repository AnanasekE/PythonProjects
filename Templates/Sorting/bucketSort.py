

def search(bucketIncrement):
    for number in arr:
        bucket = int((number - min(arr)) / bucketIncrement)
        print((number - min(arr)) / bucketIncrement)
        if number == max(arr):
            bucket -= 1
        print(bucket, arrOut[bucket], number)
        arrOut[bucket].append(number)


arr = [0.5, 0.25, 0.33, 0.4, 0.8, 1, 0, 0.22, 0.1, 0.17,0.61,0.6]
arrOut = []
list1 = []

bucketCount = 5
bucketIncrement = (max(arr) - min(arr)) / bucketCount

for g in range(bucketCount):
    arrOut.append([])

search(bucketIncrement)

for f in range(bucketCount):
    arrOut[f].sort()

print(arrOut)
