import math

a = int(input())
b = map(int, input().split())
N = math.prod(b)

c = int(input())
d = map(int, input().split())
M = math.prod(d)

print(str(math.gcd(N, M))[-9:])
