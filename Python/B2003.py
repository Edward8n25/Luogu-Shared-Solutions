# B2003-输出第二个整数
# 解法一：
num_list = input().split()
print(num_list[1])
# 解法二：
import sys
a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print(b)
