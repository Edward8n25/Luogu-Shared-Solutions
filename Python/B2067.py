# B2067-药房管理
m = float(input())
n = int(input())
num_list = list(map(float, input().split()))
fail_num = 0
for i in range(0, n):
    # 每次循环前检查所需的药物是否够用，够用则交付
    if(m - num_list[i] >= 0):
        m -= num_list[i]
    # 不够，给没取到药的人计数
    else:
        fail_num += 1
        continue
print(fail_num)