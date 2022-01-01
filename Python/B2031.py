# B2031-计算三角形面积
# 已知三边，利用海伦公式求解面积
list = input().split()
x1 = float(list[0])
y1 = float(list[1])
x2 = float(list[2])
y2 = float(list[3])
x3 = float(list[4])
y3 = float(list[5])
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("%.2f" % s)