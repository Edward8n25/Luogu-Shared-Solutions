# B2011-计算分数的浮点数值
# 解法一：
num_list = input().split()
divisor = int(num_list[0])
number = int(num_list[1])
solution = divisor / number
print("%.9f" % (solution))
# 解法二：
import sys
a, b = int(sys.argv[1]), int(sys.argv[2])
print("%.9f" % (a / b))