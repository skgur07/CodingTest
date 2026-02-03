import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    color_range = [list(map(int, input().split())) for _ in range(N)]
    color_map = [[0] * 10 for _ in range(10)]

    for my_count in range(N):
        for i in range(color_range[my_count][0], color_range[my_count][2]+1):# range(2,3)
            for j in range(color_range[my_count][1], color_range[my_count][3]+1): #(4 5)
                color_map[i][j] += color_range[my_count][4]

    print(f"#{test_case} { len([i for i in range(10) for j in range(10) if color_map[i][j] >= 3])}")
