# B2070-计算分数加减表达式的值
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += ((-1) ** (i - 1)) * (1 / i)
print("%.4f" % sum)