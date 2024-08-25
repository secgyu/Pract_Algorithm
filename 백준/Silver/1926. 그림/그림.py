import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for x2, y2 in [[x-1,y], [x+1, y], [x, y-1], [x, y+1]]:
        if 0 <= x2 < N and 0 <= y2 < M and visited[x2][y2] == False and grid[x2][y2] == 1:
            dfs(x2, y2)

N, M = map(int, input().split())

grid = []
visited = [[False]*(M) for _ in range(N)]
result = []
count = 0

for _ in range(N):
    a = list(map(int, input().split()))
    grid.append(a)

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and grid[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))

