# B2047-分段函数
x = float(input())
if x >= 0 and x < 5:
    y = -1 * x + 2.5
    print("%.3f" % y)
elif x >= 5 and x < 10:
    y = 2 - 1.5 * (x - 3) * (x - 3)
    print("%.3f" % y)
elif x >= 10 and x < 20:
    y = x / 2 - 1.5
    print("%.3f" % y)