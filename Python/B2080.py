# B2080-计算多项式的值
number = input().split()
x = float(number[0])
n = int(number[1])
sum = (1 - 1.0 * x ** (n + 1)) / (1 - x)
print("%.2f" % sum)
