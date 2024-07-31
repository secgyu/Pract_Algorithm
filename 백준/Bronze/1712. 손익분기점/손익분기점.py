import sys
input = sys.stdin.read
data = input().split()

A = int(data[0])
B = int(data[1])
C = int(data[2])

if B >= C:
    print(-1)

else:
    x = A // (C - B) + 1
    print(x)
