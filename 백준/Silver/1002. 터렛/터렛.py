import math


def find_num(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if dist == 0 and r1 == r2:
        return -1

    if dist > r1 + r2 or dist < abs(r1 - r2):
        return 0

    if dist == r1 + r2 or dist == abs(r1 - r2):
        return 1

    return 2


T = int(input())
result = []

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    result.append(find_num(x1, y1, r1, x2, y2, r2))

for i in result:
    print(i)
