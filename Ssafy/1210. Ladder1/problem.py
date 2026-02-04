import sys

sys.stdin = open('input.txt', 'r')

#  왼쪽 오른쪽 아래
dx = [0, 0, 1]
dy = [-1, 1, 0]

for _ in range(1):
    N = 100
    
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data = [row[::-1] for row in data[::-1]]

    for i in range(N):
        if data[0][i] == 2:
            
            
            x, y = 0, i
            count = 0
            while x < N :
                
                for dis in range(3):
                    nx = x + dx[dis]
                    ny = y + dy[dis]

                    if not (0 <= nx < N and 0 <= ny < N) or data[nx][ny] == 0:
                        continue
                    
                    if data[nx][ny]:
                        data[x][y] = 0
                        x, y = nx, ny
                        break
    

    result = N - y - 1
    print(f"#{tc} {result}")