import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    arr = list(map(int, input().split()))

    # 최소값과 최대값을 맨 처음 값으로 설정
    min_num = arr[0]
    max_num = arr[0]

    # min과 max 한번에 구하기
    for num in arr:
        if num < min_num:
            min_num = num

        if num > max_num:
            max_num = num

    result = max_num - min_num
    print(f"#{test_case} {result}")

