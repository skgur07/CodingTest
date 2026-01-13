
a = int(input())

if a == 1:
    print("1/1")
    exit()

line = 0
for line in range(1, 10000000):
    a -= line
    if (a - (line+1) <= 0):
        break

top = 1
bottom = line+1

for i in range(a-1):
    top += 1
    bottom -= 1

if (line+1)%2==0:
    print(f"{top}/{bottom}")
else:
    print(f"{bottom}/{top}")