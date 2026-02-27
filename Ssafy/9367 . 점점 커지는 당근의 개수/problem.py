import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    _ = input()
    ls = list(map(int, input().split()))

    result = 0
    leng = 1
    for i in range(len(ls)-1):
        if ls[i] < ls[i+1]:
            leng += 1
        else:
            result = max(leng, result)
            leng = 1

    result = max(leng, result)
    print(f"#{tc} {result}")