import sys

sys.stdin = open('/Users/skgur/Desktop/CodingTest/SSAFY/9490. 풍선팡/input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 윗쪽, 왼쪽, 아래쪽, 오른쪽
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            stage_sum = matrix[i][j]
            for k in range(4):

                for l in range(1, matrix[i][j] + 1):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l

                    if 0 <= ni < N and 0 <= nj < M:
                        stage_sum += matrix[ni][nj]

            if max_sum < stage_sum:
                max_sum = stage_sum

    print(f"#{test_case} {max_sum}")
    