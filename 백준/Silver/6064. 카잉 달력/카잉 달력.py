import sys
input = sys.stdin.readline


def calinder(M, N, x, y):
    for i in range(x, M*N+1, M):
        if (i-y) % N == 0:
            return i
    return -1


T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(calinder(M, N, x, y))
