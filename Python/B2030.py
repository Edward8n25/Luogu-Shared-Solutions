# B2030-计算线段长度
a = input().split()
b = input().split()
Xa = float(a[0])
Ya = float(a[1])
Xb = float(b[0])
Yb = float(b[1])
print("%.3f" % ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** (1 / 2))