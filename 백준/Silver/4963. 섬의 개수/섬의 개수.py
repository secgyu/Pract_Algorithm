import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[x][y] = True
    for x2, y2 in [[x-1,y], [x+1, y], [x, y-1], [x, y+1], 
                   [x+1, y-1], [x+1, y+1], [x-1, y-1], [x-1, y+1]]:
        if 0 <= x2 < h and 0 <= y2 < w and visited[x2][y2] == False and grid[x2][y2] == 1:
            dfs(x2, y2)

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    grid = []
    visited = [[False]*(w) for _ in range(h)]
    for _ in range(h):
        grid.append(list(map(int, input().split())))

    count = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and grid[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)