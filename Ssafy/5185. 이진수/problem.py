import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    _, hex_num = input().split()

    print(f"#{tc} {''.join(bin(int(hex_num, 16)).split('b')[1]).zfill(len(hex_num) * 4)}")