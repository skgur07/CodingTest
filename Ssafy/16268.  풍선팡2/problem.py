import sys

sys.stdin = open('input.txt', 'r')


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    stage_sum = 0
    total_sum = 0
    for i in range(N):
        for j in range(M):
            stage_sum = matrix[i][j]
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    stage_sum += matrix[nx][ny]

            total_sum = max(total_sum, stage_sum)

    print(f'#{tc} {total_sum}')                