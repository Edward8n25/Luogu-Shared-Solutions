# B2039-整数大小比较
list = input().split()
x = int(list[0])
y = int(list[1])
if x > y:
    print(">")
elif x == y:
    print("=")
elif x < y:
    print("<")