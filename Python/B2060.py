# B2060-满足条件的数累加
m, n = map(int, input().split())
sum = 0
for i in range(m, n + 1):
    if i % 17 == 0:
        sum += i
print(sum)