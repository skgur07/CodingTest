import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    num = input()
    leng = len(num.split('.')[1])
    num = float(num)
    result = ''
    cnt = 0
    
    for i in range(1, leng + 1):

        if cnt >= 12:
            result = 'overflow'
            break

        if num - pow(2, i * -1) >= 0:
            num -= pow(2, i * -1)
            result += '1'
        
        else:
            result += '0'

        cnt += 1

    if num:
        result = 'overflow'

    print(f"#{tc} {result}")