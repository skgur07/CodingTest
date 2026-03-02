a = list(map(int, input()))
b = list(map(int, input()))

la = list(reversed(a))
lb = list(reversed(b))

for i in range(len(lb)):
    result = 0
    ten = 1
    for j in range(len(la)):
        result += la[j] * lb[i] * ten
        ten *= 10
    print(result)

print(int(''.join(map(str, a))) * int(''.join(map(str, b))))