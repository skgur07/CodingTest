import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for i in range(N)]
    result = 0
    # x, y = 다음 움직일 곳, point = 있는 곳의 값, used = K를 사용했는지 안 했는지
    def dfs(x, y, used, length):
        nonlocal result
        result = max(result, length)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and matrix[x][y] > matrix[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, used, length + 1)
                    visited[nx][ny] = False
                elif not used and not visited[nx][ny] and matrix[nx][ny] - K < matrix[x][y]:
                    real = matrix[nx][ny]
                    matrix[nx][ny] = matrix[x][y] - 1
                    
                    visited[nx][ny] = True
                    dfs(nx, ny, 1, length + 1)
                    visited[nx][ny] = False
                    
                    matrix[nx][ny] = real

    max_value = max(max(row) for row in matrix)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_value:
                visited[i][j] = True
                dfs(i, j, 0, 1)
                visited[i][j] = False
    print(result)