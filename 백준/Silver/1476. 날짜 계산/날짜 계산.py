import sys
input = sys.stdin.readline


def find_year(E, S, M):
    e, s, m = 1, 1, 1
    year = 1

    while True:
        if e == E and s == S and m == M:
            return year
        e = e+1 if e < 15 else 1
        s = s+1 if s < 28 else 1
        m = m+1 if m < 19 else 1
        year += 1


E, S, M = map(int, input().split())
print(find_year(E, S, M))
