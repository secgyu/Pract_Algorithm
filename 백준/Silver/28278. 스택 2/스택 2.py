import sys
input = sys.stdin.readline
N = int(input())

stack = []

for _ in range(N):
    what = list(map(int, input().split()))

    if what[0] == 1:
        stack.append(what[1])

    elif what[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif what[0] == 3:
        print(len(stack))

    elif what[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif what[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
