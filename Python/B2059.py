# B2059-奇数求和
m, n = map(int, input().split())
sum = 0
for i in range(m, n + 1):
    if i % 2 == 1:
        sum += i
print(sum)