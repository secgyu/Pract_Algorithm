import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

seq = deque(enumerate(map(int, input().split())))

result = []

while seq:
    index, paper = seq.popleft()
    result.append(index + 1)

    if paper > 0:
        seq.rotate(-(paper - 1))
    else :
        seq.rotate(-paper)

print(*result)