import sys

sys.stdin = open('input.txt', 'r')

def square(n, m, i):
    if i >= m:
        return 1
    return n * square(n, m , i + 1)

for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    
    print(f'#{tc} {square(n, m, 0)}')
    