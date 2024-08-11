import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
A = list(map(int, input().split()))

ans = [-1] * n
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

output(" ".join(map(str, ans)) + "\n")
