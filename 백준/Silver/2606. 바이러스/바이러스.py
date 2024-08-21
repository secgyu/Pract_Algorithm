def dfs(i):
    visited[i] = True
    for j in graph[i] :
        if not visited[j]:
            dfs(j)

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for i in range(E):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited)-1)