import math
import sys
input = sys.stdin.readline

min_num, max_num = map(int, input().split())
arr = [0] * (10000001)

for i in range(2, len(arr)):
    arr[i] = i

for i in range(2, int(math.sqrt(len(arr))+1)):
    if arr[i] == 0:
        continue

    for j in range(i+i, len(arr), i):
        arr[j] = 0

count = 0

for i in range(2, 10000001):
    if arr[i] != 0:
        temp = arr[i]
        while arr[i] <= max_num / temp:
            if arr[i] >= min_num / temp:
                count += 1
            temp = temp * arr[i]
print(count)