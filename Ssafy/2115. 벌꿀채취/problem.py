import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')

T = int(input())


def in_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return 1
    return 0


def total(honeys):
    big_money = 0
    for i in range(len(honeys) + 1):
        for j in combinations(honeys, i):
            tmp_money = 0
            if sum(j) <= C:
                for k in j:
                    tmp_money += k * k
                big_money = max(tmp_money, big_money)
    return big_money


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())

    honey_map = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    honeyA = []
    honeyB = []
    # 첫번째 양봉자
    for i in range(N):
        for j in range(N - M + 1):

            # 두번째 양봉자
            for x in range(i, N):
                for y in range(N - M + 1):
                    if x == i and y < j + M:
                            continue
                    # if in_range(j + M, y + M):
                        
                    honeyA = []
                    honeyB = []
                    for move in range(M):
                        honeyA.append(honey_map[i][j + move])
                        honeyB.append(honey_map[x][y + move])

                    result = max(total(honeyA) + total(honeyB), result)

    print(f'#{tc} {result}')