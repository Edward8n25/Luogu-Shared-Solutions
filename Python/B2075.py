# B2075-幂的末尾
a, b = map(int, input().split())
c = a ** b
print("%03d" % (c % 1000))
