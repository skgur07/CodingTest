from itertools import combinations

def solution(number):
    result = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            result += 1
    return result