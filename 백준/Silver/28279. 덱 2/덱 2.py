import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
d = deque()

for _ in range(N):
    what = list(map(int, input().split()))

    if what[0] == 1:
        d.appendleft(what[1])

    elif what[0] == 2:
        d.append(what[1])

    elif what[0] == 3:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())

    elif what[0] == 4:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())

    elif what[0] == 5:
        print(len(d))

    elif what[0] == 6:
        if len(d) == 0:
            print(1)
        else:
            print(0)

    elif what[0] == 7:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])

    elif what[0] == 8:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
