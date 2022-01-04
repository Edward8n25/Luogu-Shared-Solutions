# B2079-求出 e 的值
n = int(input())
e = 1.0
for i in range(1, n + 1):
    x = 1
    for j in range(1, i + 1):
        x *= j
    e += (1.0 / x)
print("%.10f" % e)
