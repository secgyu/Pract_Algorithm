import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    num = int(input())

    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)