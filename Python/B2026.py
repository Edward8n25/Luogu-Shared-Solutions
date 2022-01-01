# B2026-计算浮点数相除的余
num_list = input().split()
a = float(num_list[0])
b = float(num_list[1])
k = int(a / b)
print(a - k * b)