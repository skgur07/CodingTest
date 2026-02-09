import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m  = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(m):
        arr.append(arr.pop(0))
    
    print(f'{tc} {arr[0]}')