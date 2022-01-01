# B2056-求整数的和与均值
n = int(input())
sum = 0
for i in range(0, n):
    num = int(input())
    sum += num
print("%d %.5lf" % (sum, sum / n))