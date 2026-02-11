import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    
    result = []
    primes = [2, 3, 5, 7, 11]

    
    for prime in primes:
        cnt = 0
        while True:
            if not num % prime:
                cnt += 1
                num //= prime
                continue
            result.append(cnt)
            break

    print(f"#{tc}", *result)