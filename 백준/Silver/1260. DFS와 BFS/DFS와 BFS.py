from collections import deque

# 정점에 개수(노드) // 간선의 개수 (노드 연결 선) // 탐색을 시작할 번호
N, M, V = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]

for mom_node, bro_node in info:
    graph[mom_node].append(bro_node)
    graph[bro_node].append(mom_node)

for i in range(len(graph)):
    graph[i].sort()


def dfs(v):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(V):
    que = deque([V])
    visited[V] = True
    
    while que:
        node = que.popleft()
        print(node, end = ' ')

        for i in graph[node]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)
