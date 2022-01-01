# B2054-求平均年龄
n = int(input())
s = []
for i in range(0, n):
    s.append(int(input()))
a = sum(s) / len(s)
print("%.2f" % a)