
end = int(input())

for i in range(1, end + 1):
    str_i = str(i)

    if str_i.count('3') or str_i.count('6') or str_i.count('9') > 0:
            print('-' * (str_i.count('3') + str_i.count('6') + str_i.count('9')), end = '')
            print(end = ' ')
            continue
    print(i, end = ' ')