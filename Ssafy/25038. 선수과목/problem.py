
import sys
sys.stdin = open('input.txt', 'r')

from collections import defaultdict, deque

T = int(input())


for tc in range(1, T + 1):
    graph = defaultdict(list)
    
    N = int(input())
    degree = [0] * (N + 1)
    sem = [0] * (N + 1)

    for i in range(1, N + 1):
        node = list(map(int, input().split()))
        cnt = node[0]
        pre = node[1:]
        degree[i] = cnt
        
        for p in pre:
            graph[p].append(i)

    que = deque()
    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)
            sem[i] = 1

    cnt = 0
    while que:
        cur = que.popleft()
        cnt += 1
        for nxt in graph[cur]:
            degree[nxt] -= 1
            sem[nxt] = max(sem[nxt], sem[cur] + 1)
            
            if degree[nxt] == 0:
                que.append(nxt)

    result = max(sem)
    if cnt != N: result = -1
    print(f"#{tc} {result}")