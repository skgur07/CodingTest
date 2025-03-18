def solution(my_string, alp):
    answer = ''
    for _ in my_string:
        if _ == alp:
            _ = alp.upper()
        answer += _

    return answer

