import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

c = 1
def dfs(v, e, i):
    global c
    visited[i] = c
    for j in graph[i]:
        if visited[j] == 0:
            c+=1
            dfs(v, e, j)

v, e, s = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)

for _ in range(e):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(v+1):
    graph[i].sort()

dfs(v, e, s)

for i in range(1,v+1):
    print(visited[i])
