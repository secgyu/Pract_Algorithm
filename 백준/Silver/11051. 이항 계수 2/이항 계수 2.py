import math

n, k = map(int, input().split())

tmp = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
result = tmp % 10007
print(result)
