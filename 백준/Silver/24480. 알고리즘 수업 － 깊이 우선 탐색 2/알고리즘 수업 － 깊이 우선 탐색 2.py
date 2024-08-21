import sys
sys.setrecursionlimit(10**7 + 1)
input = sys.stdin.readline


def dfs(i):
    global cnt
    visited[i] = True
    result[i] = cnt
    graph[i].sort(reverse=True)
    for j in graph[i] :
        if not visited[j]:
            cnt += 1
            dfs(j)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)
cnt = 1

for _ in range(m):
    x, y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for i in result[1:]:
    print(i)