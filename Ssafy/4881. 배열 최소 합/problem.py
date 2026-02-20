import sys
from itertools import permutations # , combinations
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    idx = [i for i in range(N)]
    min_number = float('inf')
    for pers in permutations(idx, N):
        tmp = 0
        for i, per in enumerate(pers):
            tmp += matrix[i][per]
            if tmp > min_number:
                break
        min_number = min(tmp, min_number)
    print(f"#{tc} {min_number}")