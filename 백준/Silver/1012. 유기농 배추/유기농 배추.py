import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[x][y] = True
    for x2, y2 in [[x-1,y], [x+1, y], [x, y-1], [x, y+1]]:
        if 1 <= x2 <= n and 1 <= y2 <= m and visited[x2][y2] == False and grid[x2][y2] == 1:
            dfs(x2, y2)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    visited = [[False] * (m+1) for _ in range(n+1)]
    grid = [[0] * (m+1) for _ in range(n+1)]

    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y+1][x+1] = 1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not visited[i][j] and grid[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
