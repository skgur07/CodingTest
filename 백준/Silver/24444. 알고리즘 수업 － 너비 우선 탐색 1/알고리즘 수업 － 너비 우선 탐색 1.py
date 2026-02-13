import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E, R = map(int, input().split())

graph = [[] for _ in range(V + 1)]

tmp = [list(map(int, input().split())) for _ in range(E)]

for u, v in tmp:
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (V + 1)
order = [0] * (V + 1)
cnt = 1

def bfs(v):
    global cnt
    visited[v] = True
    que = deque([v])
    order[v] = cnt
    cnt += 1
    
    while que:

        vi = que.popleft()

        for i in graph[vi]:
            if not visited[i]:
                que.append(i)
                order[i] = cnt
                visited[i] = True
                cnt += 1

bfs(R)
for i in range(1, len(order)):
    print(order[i])