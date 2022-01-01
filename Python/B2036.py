# B2036-输出绝对值
n = float(input())
if n >= 0:
    print("%.2f" % n)
elif n < 0:
    n = -1 * n
    print("%.2f" % n)