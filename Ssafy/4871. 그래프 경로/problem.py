import sys

from collections import defaultdict             

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    graph = defaultdict(list)

    V, E = map(int, input().split())
    
    for _ in range(E):
        v, u = map(int, input().split())
        graph[v].append(u)

    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    
    result = 0

    def dfs(v):
        global result

        visited[v] = True

        if result:
            return

        if v == G:
            result = 1
            return

        for i in graph[v]:
            if not visited[i]:
                dfs(i)

    dfs(S)

    print(f"#{tc} {result}")