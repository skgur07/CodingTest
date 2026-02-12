import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    freight = list(map(int, input().split()))
    # 정렬 후 큰 숫자부터 가져와서 아래에 쌓기
    freight.sort()

    result = 0
    i = 1
    while True:

        if A > 0:
            # a.append(freight.pop() * i)
            result += freight.pop() * i
            A -= 1
        if B > 0:
            # b.append(freight.pop() * i) 비효율적
            result += freight.pop() * i  # 수정
            B -= 1
        if A == 0 and B == 0:
            break
        i += 1

    # result = sum(a) + sum(b)
    print(f'#{tc} {result}')
