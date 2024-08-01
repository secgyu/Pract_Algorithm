import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

d = deque()

for _ in range(N):
    what = input().split()

    if what[0] == 'push_front':
        d.appendleft(what[1])
    
    elif what[0] == 'push_back':
        d.append(what[1])
    
    elif what[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    
    elif what[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    
    elif what[0] == 'size':
        print(len(d))
    
    elif what[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    
    elif what[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    
    elif what[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])