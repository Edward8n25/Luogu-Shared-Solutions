# B2081-与 7 无关的数
n = int(input())
sum = 0
for i in range(1, n + 1):
    if i % 7 != 0 and i % 10 != 7 and i // 10 % 10 != 7:
        sum += i * i
print("%d" % sum)