import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False

    return True

N = int(input())

ls = list(map(int, input().split()))

result = 0
for i in ls:
    if is_prime(i):
        result += 1

print(result)