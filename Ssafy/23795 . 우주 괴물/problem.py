import sys

sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            
            if matrix[i][j] == 2:
                for k in range(4):
                    dis = 1
                    while True:
                        nx = i + (dx[k] * dis)
                        ny = j + (dy[k] * dis)
                        
                        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 1:
                            matrix[nx][ny] = 1
                            dis += 1
                            continue

                        break
    
    result = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                result += 1

    print(f"#{tc} {result}")