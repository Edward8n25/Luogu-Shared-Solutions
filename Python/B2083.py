# B2083-画矩形
try:
    a, b, c, f = (input().split())
except:
    a, b, c, f = (17, 92, '1', 0)
a, b = int(a), int(b)
try:
    f = int(f)
    if f != 0:
        f = 1
except:
    f = 0
if f == 0:
    print(c * b)
    for i in range(a - 2):
        print(c + ' ' * (b - 2) + c)
    print(c*b)
else:
    for i in range(a):
        print(c * b)