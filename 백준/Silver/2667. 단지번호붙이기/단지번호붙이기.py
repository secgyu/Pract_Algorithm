import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True
    for x2, y2 in [[x-1,y], [x+1, y], [x, y-1], [x, y+1]]:
        if 0 <= x2 < N and 0 <= y2 < N and visited[x2][y2] == False and grid[x2][y2] == 1:
            dfs(x2, y2)

N = int(input())

result = []
grid = []

visited = [[False]*(N) for _ in range(N)]
for _ in range(N):
    grid.append(list(map(int, input().rstrip())))

count = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False and grid[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])