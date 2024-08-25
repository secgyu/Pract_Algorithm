import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1, V+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
