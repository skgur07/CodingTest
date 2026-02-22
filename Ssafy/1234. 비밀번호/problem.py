import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    _, password = input().split()

    result = []
    for char in password:
        if not result:
            result.append(char)
            continue
        
        if (tmp := result.pop()) == char:
            continue
        else:
            result.append(tmp)
            result.append(char)

    print(f"#{tc} {''.join(result)}")