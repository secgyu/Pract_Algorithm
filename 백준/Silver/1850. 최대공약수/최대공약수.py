import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
result = math.gcd(a, b)

while result > 0:
    print(1, end='')
    result -= 1
