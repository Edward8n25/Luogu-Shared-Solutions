# B2072-分苹果
n = int(input())
sum = 0
# 每个人的数目不一样，转化为递增求和
for i in range(1, n + 1):
    sum += i
print(sum)
