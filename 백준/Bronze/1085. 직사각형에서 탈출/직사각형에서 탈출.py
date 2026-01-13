x, y, w, h = map(int, input().split())

x1, y1 = 0, 0

if(w - x > x):
    x1 = x
else:
    x1 = w - x

if(h - y > y):
    y1 = y
else:
    y1 = h - y

print(min(x1, y1))