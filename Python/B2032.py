# B2032-等差数列末项计算
list = input().split()
a1 = int(list[0])
a2 = int(list[1])
n = int(list[2])
d = a2 - a1
print(a1 + (n - 1) * d)