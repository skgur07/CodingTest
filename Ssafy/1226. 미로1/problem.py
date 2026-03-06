import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, 11):
    _ = input()

    N = 16
    matrix = [list(map(int, input())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2: 
                start = [i, j]
            if matrix[i][j] == 3: 
                end = [i, j]

    que = deque([start])

    find = 0

    while que:
        
        x, y = que.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1:
                if matrix[nx][ny] == 3:
                    find = 1
                    break

                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = 1
                    que.append([nx, ny])
                
        if find == 1:
            break
    
    print(f"#{tc} {find}")
        