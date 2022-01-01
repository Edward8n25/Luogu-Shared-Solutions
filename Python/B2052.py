# B2052-简单计算器
list = input().split()
x = int(list[0])
y = int(list[1])
c = list[2]
if c == '+':
    print(x + y)
elif c == '-':
    print(x - y)
elif c == '*':
    print(x * y)
elif c == '/':
    if y == 0:
        print("Divided by zero!")
    else:
        print(x / y)
else:
    print("Invalid operator!")