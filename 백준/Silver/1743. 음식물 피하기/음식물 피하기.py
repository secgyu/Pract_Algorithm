import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for x2, y2 in [[x-1,y], [x+1, y], [x, y-1], [x, y+1]]:
        if 1 <= x2 <= N and 1 <= y2 <= M and visited[x2][y2] == False and grid[x2][y2] == 1:
            dfs(x2, y2)

N, M, K = map(int, input().split())

grid = [[0]*(M+1) for _ in range(N+1)]
visited = [[False]*(M+1) for _ in range(N+1)]
result = []
count = 0

for _ in range(K):
    a, b = map(int, input().split())
    grid[a][b] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        if visited[i][j] == False and grid[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)
print(max(result))

