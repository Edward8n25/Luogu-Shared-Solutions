# B2076-球弹跳高度的计算
h = int(input())
sum = h
for i in range(1, 10):
    h = h / 2
    sum += (2 * h)
print(sum)
print(h / 2)
