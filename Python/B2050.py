# B2050-三角形判断
list = input().split()
a = int(list[0])
b = int(list[1])
c = int(list[2])
if a + b > c and a + c > b and b + c > a:
    print(1)
else:
    print(0)