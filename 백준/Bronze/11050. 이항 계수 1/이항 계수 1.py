import sys
import math

input = sys.stdin.readline
n, k = map(int, input().split())

result1 = math.factorial(n)
tmp = n - k
result2 = math.factorial(tmp)
result3 = math.factorial(k)
tmp2 = result2 * result3

result = result1 / tmp2

print(int(result))
