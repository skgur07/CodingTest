import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    arr = list(map(int, input()))

    num_set = [0] * 10

    max_count = 0
    max_num = 0

    # 1부터 9까지 카운트하고 카운트 값이 최대와 같다면 i 저장
    for i in range(10):
        if arr.count(i) >= max_count:
            # 가장 큰 카드 값 찾음
            max_count = arr.count(i)
            max_num = i

    print(f"#{test_case} {max_num} {max_count}")