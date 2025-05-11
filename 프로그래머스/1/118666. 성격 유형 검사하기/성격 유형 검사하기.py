def solution(survey, choices):
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    point = [3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        if choices[i] <= 3:
            dic[survey[i][0]] += point[choices[i]-1]
        elif choices[i] >= 5:
            dic[survey[i][1]] += point[choices[i]-1]
        
    dic_list = list(dic.keys())
    dic_values = list(dic.values())

    result = ''

    for i in range(0, len(dic), 2):
        if dic_values[i] >= dic_values[i+1]:
            result += dic_list[i]
        else:
            result += dic_list[i+1]

    return result
