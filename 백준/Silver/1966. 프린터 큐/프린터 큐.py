import sys
from collections import deque

t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    priorities = list(map(int, sys.stdin.readline().strip().split()))
    queue = deque((i, priorities[i]) for i in range(n))
    count = 0

    while queue:
        current = queue.popleft()
        
        if any(current[1] < item[1] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[0] == m:
                print(count)
                break
