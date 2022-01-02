# B2063-人口增长问题
x, n = map(int, input().split())
print("%.4lf" % (x * (1.001 ** n)))