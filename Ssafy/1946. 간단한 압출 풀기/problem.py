import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    
    number = int(input())

    arr = [list(input().split()) for _ in range(number)]

    string = ''

    for myStr, i in arr:
        string += myStr * int(i)

    print(f"#{tc}")
    for i, result in enumerate(string, start = 1):

        print(result, end = '')
        if i % 10 == 0:
            print()
