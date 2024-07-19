import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
result = math.lcm(a, b)
print(result)
