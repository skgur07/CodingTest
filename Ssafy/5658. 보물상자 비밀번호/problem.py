import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    fig = input()

    all_case = []
    side = N // 4

    for i in range(side):
        for j in range(0, N, side):
            if int(fig[j:j+side], 16) not in all_case:
                all_case.append(int(fig[j:j+side], 16))
        fig = fig[-1] + fig[:N-1]


    all_case.sort(reverse = True)

    print(f'#{tc} {all_case[K-1]}')