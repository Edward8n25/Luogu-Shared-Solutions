# B2029-大象喝水
import math
new_list = input().split()
h = int(new_list[0])
r = int(new_list[1])
PI = 3.1415926
v = PI * r * r * h
# 利用ceil函数取得不小于math的最小整数，即向上取整
num = math.ceil(20 * 1000 / v)
print(num)