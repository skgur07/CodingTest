import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(total, depth):
    global result

    if total > result:
        return

    if depth == N:
        if total >= B:
            result = min(total, result)
            
        return
    
    dfs(total + heights[depth], depth + 1)
    dfs(total, depth + 1)


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    
    result = float('inf')
    dfs(0, 0)
    
    print(f"#{tc} {result - B}")


# 처음풀때 코드

# def dfs(idx, sum):
#     result.append(sum)
#     for i in range(idx + 1, n):
#         dfs(i, sum + ls[i])

# t = int(input())

# for count in range(t):

#     n, b = map(int, input().split())
#     ls = list(map(int, input().split()))

#     result = []

#     for i in range(n):
#         dfs(i, ls[i])

#     answer = [i for i in result if i >= b]

#     print(f"#{count+1} {min(answer) - b}")

