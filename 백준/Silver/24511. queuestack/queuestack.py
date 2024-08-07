import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

seq_A = list(map(int, input().split()))
seq_B = list(map(int, input().split()))
M = int(input())
seq_C = list(map(int, input().split()))

queue = deque([])

for i in range(N):
    if seq_A[i] == 0:
        queue.append(seq_B[i])

for i in range(M):
    item = seq_C[i]
    queue.appendleft(item)
    print(queue.pop(), end= ' ')