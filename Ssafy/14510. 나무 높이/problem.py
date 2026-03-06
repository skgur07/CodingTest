import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree_list = list(map(int, input().split()))

    max_h = max(tree_list)

    one = 0
    two = 0

    for h in tree_list:
        diff = max_h - h
        one += diff % 2
        two += diff // 2

    while two > one + 1:
        two -= 1
        one += 2
    
    if one > two: result = one * 2 - 1
    else: result = two * 2

    print(f"#{tc} {result}")