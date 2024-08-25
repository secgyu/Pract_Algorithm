import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            result[i] = v
            dfs(i)

V = int(input())

graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
result = [0] * (V+1)

for _ in range(V-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2,V+1):
    print(result[i])