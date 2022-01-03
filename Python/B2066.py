# B2066-救援
import math
k = int(input())
sum_time = 0
for i in range(0, k):
    # 使用浮点数保证精度
    num_list = list(map(float, input().split()))
    t1 = math.sqrt(num_list[0] ** 2 + num_list[1] ** 2) * 2
    t2 = num_list[2] * 1.5
    sum_time += t1 / 50 + t2
# 一定要最后再取整，否则误差会很大
print(math.ceil(sum_time))

'''
# 错误的样例
import math
k = int(input())
sum_time = []
for i in range(0, k):
    num_list = list(map(float, input().split()))
    t1 = math.sqrt(num_list[0] ** 2 + num_list[1] ** 2) / 50
    t2 = num_list[2] * 1.5
    sum_time.append(int(math.ceil(2 * t1 + t2)))
print(sum(sum_time))
'''

'''
# 正确的样例
import math
k = int(input())
sum_time = []
for i in range(0, k):
    num_list = list(map(float, input().split()))
    t1 = math.sqrt(num_list[0] ** 2 + num_list[1] ** 2) / 50
    t2 = num_list[2] * 1.5
    sum_time.append(2 * t1 + t2)
print(math.ceil(sum(sum_time)))
'''