def solution(n):
    answer = ''
    check  = 0
    if (n % 2 == 1):
        check = 1
    for i in range(n // 2):
        answer += '수박'
    
    if (check == 1):
        answer += '수'
        
    return answer