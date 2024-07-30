import math

case = int(input())

for _ in range(case):
    nums = list(map(int, input().split()))

    max_gcd = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a, b = nums[i], nums[j]
            result = math.gcd(a, b)

            if max_gcd < result:
                max_gcd = result

    print(max_gcd)
