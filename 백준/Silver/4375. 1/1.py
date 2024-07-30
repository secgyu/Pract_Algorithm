import sys


def multiple(n):
    remain = 0
    length = 0

    for i in range(1,10001):
        remain = (remain * 10 + 1) % n
        length += 1

        if remain == 0:
            return i


n = map(int, sys.stdin.read().split())

for i in n:
    if i:
        n = int(i)
        print(multiple(n))
