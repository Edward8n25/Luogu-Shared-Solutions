# B2010-带余除法
num_list = input().split()
divisor = int(num_list[0]) # 被除数
number = int(num_list[1]) # 除数
solution = divisor // number # 整数商
remain = divisor % number # 余数
print("%d %d" % (solution, remain))
