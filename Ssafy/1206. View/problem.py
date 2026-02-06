import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    ap_list = list(map(int, input().split()))

    all_light = 0
    for i in range(2, n - 2):
        max_light = 0
        for j in range(1, 3):
            max_light = max(max_light, ap_list[i + j], ap_list[i-j])   
        if max_light > ap_list[i]:
            continue
        all_light += ap_list[i] - max_light

    print(f'#{tc} {all_light}')