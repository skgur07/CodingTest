import sys

sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())

    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    
    result = 0
    for i in range(N):
        row = 0
        col = 0
        for j in range(N):
            row += matrix[i][j]
            col += matrix[j][i]
        result = max(row, result, col)    

    main_diagonal = 0
    sub_diagonal = 0
    for i in range(N):
        main_diagonal += matrix[i][i]
        sub_diagonal += matrix[i][N - i - 1]
    
    result = max(main_diagonal, sub_diagonal, result)
    
    print(f'#{tc} {result}')