# B2015-计算并联电阻的阻值
num_list = input().split()
r1 = float(num_list[0])
r2 = float(num_list[1])
R = 1 / (1 / r1 + 1 / r2)
print("%.2f" % R)