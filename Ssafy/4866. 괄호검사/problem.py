import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

mapper = {
    '}' : '{',
    ']' : '[',
    ')' : '('
}

for tc in range(1, T + 1):
    text = input()
    result = 1
    stack = []

    
    for char in text:
        
        if char in mapper.values():
            stack.append(char)
            continue
        

        elif char in mapper.keys():    
            if stack:
                if stack.pop() == mapper[char]:
                    continue
                else:
                    result = 0
                    break
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')
