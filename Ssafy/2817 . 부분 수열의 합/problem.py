import sys
from itertools import combinations

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = 0
    for i in range(1, N + 1):
        for j in combinations(A, i):
            if sum(j) == K:
                result += 1


    print(f"#{tc} {result}")