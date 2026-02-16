import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

# 가로 새로
dgx = [-1, 0, 1, 0]
dgy = [0, 1, 0, -1]

# 대각선
ddx = [-1, 1, 1, -1]
ddy = [1, -1, 1, -1]

def in_range(nx, ny):
    if 0 <= nx < N and 0 <= ny < N:
        return 1
    return 0

T = int(input())
for tc in range(1, T + 1):

    # N * N 배열 // M의 세기
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    plu_sum = 0
    mul_sum = 0
    result = 0
    for i in range(N):
        for j in range(N):
            
            # 움직임
            plu_sum, mul_sum = matrix[i][j], matrix[i][j]
            
            # 얼만큼 갈지
            for move in range(1, M):
                for k in range(4):    
                    
                    # 가로 새로
                    nx1 = i + (dgx[k] * move)
                    ny1 = j + (dgy[k] * move)

                    if in_range(nx1, ny1):
                        # print(nx1, ny1)
                        plu_sum += matrix[nx1][ny1]
                    
                    # 대각선
                    nx2 = i + (ddx[k] * move)
                    ny2 = j + (ddy[k] * move)

                    if in_range(nx2, ny2):
                        mul_sum += matrix[nx2][ny2]

            # print(i, j, plu_sum)
            # print(mul_sum)       
            result = max(plu_sum, mul_sum, result)

    print(f"#{tc} {result}")