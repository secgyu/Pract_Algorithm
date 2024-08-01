import sys
input = sys.stdin.readline

N = int(input())
stack = []


for _ in range(N):
    what = input().split()

    if what[0] == 'push':
        stack.append(what[1])

    elif what[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif what[0] == 'size':
        print(len(stack))

    elif what[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif what[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
