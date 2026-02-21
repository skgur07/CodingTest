from itertools import permutations

import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def permutations(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    
    for i in range(len(arr)):
        elem = arr[i]
        
        for reset in permutations(arr[:i] + arr[i + 1:], n - 1):
            result.append([elem] + reset)

    return result

def is_run(cards):
    cards = list(map(int, cards))
    cards.sort()
    return cards[0] + 1 == cards[1] and cards[1] + 1 == cards[2] 

def is_triplet(cards):
    return cards[0] == cards[1] == cards[2]

for tc in range(1, T + 1):
    result = 'false'
    cards = list(input())
    
    for i in permutations(cards, 6):
        if (is_run(i[:3]) or is_triplet(i[:3])) and (is_run(i[3:]) or is_triplet(i[3:])):
            result = 'true'
            break

    print(f'#{tc} {result}')