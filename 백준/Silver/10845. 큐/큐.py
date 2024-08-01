import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N):
    what = input().split()

    if what[0] == 'push':
        queue.append(what[1])

    elif what[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif what[0] == 'size':
        print(len(queue))

    elif what[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif what[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif what[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
