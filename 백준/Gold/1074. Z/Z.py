import sys

n, r, c = map(int, sys.stdin.readline().split())

visit = 0
while n != 0:
    n -= 1
    size = 2 ** n

    # 1사분면
    if r < size and c < size:
        visit += 0

    # 2사분면
    elif r < size and c >= size:
        visit += size * size
        c -= size

    # 3사분면
    elif r >= size and c < size:
        visit += size * size * 2
        r -= size

    # 4사분면
    else:
        visit += size * size * 3
        r -= size
        c -= size

print(visit)