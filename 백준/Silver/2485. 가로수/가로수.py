import sys
import math
input = sys.stdin.readline

n = int(input())
a = int(input())

A = []

for i in range(n-1):
    num = int(input())
    A.append(num - a)
    a = num

g = A[0]
for i in range(1, len(A)):
    g = math.gcd(g, A[i])
result = 0

for each in A:
    result += each // g-1
print(result)