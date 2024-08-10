from collections import deque

N, M = map(int, input().split())
positions = list(map(int, input().split()))

deque = deque(range(1, N+1))
count = 0

for i in positions:
    index = deque.index(i)

    if index <= len(deque) // 2:
        count += index
        deque.rotate(-index)
    
    else:
        count += len(deque) - index
        deque.rotate(len(deque) - index)
    
    deque.popleft()
print(count)
