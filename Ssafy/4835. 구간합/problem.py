
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    total_max = 0
    total_min = sum(numbers)
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            
            tmp += numbers[i+j]
        total_max = max(tmp, total_max)
        total_min = min(tmp, total_min)
    
    
    print(f'#{test_case} {total_max - total_min}')

# 8, 6 