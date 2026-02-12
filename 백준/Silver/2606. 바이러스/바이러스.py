from collections import deque

all_computer = int(input())

n = int(input())
graph = [[] for _ in range(all_computer + 1)]


connection = [list(map(int, input().split())) for _ in range(n)]

for i, j in connection:
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (all_computer + 1)
cnt = 0

def bfs(v):
    global cnt
    
    computer = deque([v])
    
    visited[v] = True

    while computer:

        visited_computer = computer.popleft()

        for i in graph[visited_computer]:
            if not visited[i]:
                computer.append(i)
                visited[i] = True
                cnt += 1

    return cnt

print(bfs(1))
