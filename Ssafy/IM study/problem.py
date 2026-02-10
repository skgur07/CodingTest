import sys

sys.stdin = open('input.txt', 'r')


def in_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return 1
    return 0


T = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())

    height_map = [list(map(int, input().split())) for _ in range(N)]

    # max_number = max(height_map)
    max_number = max([height_map[i][j] for i in range(N) for j in range(N)])

    result = 0
    for i in range(N):
        for j in range(N):

            if height_map[i][j] == max_number:
                cnt = 1
                x, y = i, j
                while True:
                    check = []

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if in_range(nx, ny):
                            if height_map[x][y] > height_map[nx][ny]:
                                check.append([height_map[nx][ny], nx, ny])
                                continue

                    if not check:
                        break

                    value = check[0][0]
                    for number, nx, ny in check:
                        if number <= value:
                            x = nx
                            y = ny
                    cnt += 1
                result = max(cnt, result)


    print(f'#{tc} {result}')
