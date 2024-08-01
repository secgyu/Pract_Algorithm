import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])

seq = []

while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())

    seq.append(str(deq.popleft()))

print('<'+', '.join(seq)+'>')
