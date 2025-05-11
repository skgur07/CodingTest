def solution(num_list):
    s1 = ''
    s2 = ''
    
    for i in num_list:
        if i % 2 == 0:
            s1 += str(i)
        else:
            s2 += str(i)
    
    return int(s1) + int(s2)