# B2082-数字统计
n = list(map(int, input().split()))
s = 0
for i in range(n[0], n[1] + 1):
    i = str(i)
    s += i.count('2')
print(s)