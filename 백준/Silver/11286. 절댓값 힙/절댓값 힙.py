import heapq
import sys
input = sys.stdin.readline

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)