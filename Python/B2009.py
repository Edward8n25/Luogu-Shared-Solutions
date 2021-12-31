# B2009-计算 (a+b)/c 的值
num_list = input().split()
# 注意此处的除法是整除运算不是浮点数除法
print((int(num_list[0]) + int(num_list[1])) // int(num_list[2]))
