import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]

for u, v in arr:
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort(reverse = True)
    
visited = [False] * (N + 1)

order = [0] * (N + 1)
cnt = 1
def dfs(v):
    global cnt
    visited[v] = True
    order[v] = cnt
    cnt += 1
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(R)


for i in range(1, N + 1):
    print(order[i])