import math
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    result = math.factorial(m) / (math.factorial(n) * math.factorial(m-n))
    print(int(result))
