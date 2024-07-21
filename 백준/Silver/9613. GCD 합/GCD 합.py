import math

case = int(input())

for i in range(case):
    arr = list(map(int, input().split()))
    sum = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            sum += math.gcd(arr[j], arr[k])
    print(sum)
