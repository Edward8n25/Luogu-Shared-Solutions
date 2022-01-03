# B2068-统计满足条件的 4 位数
n = int(input())
num_list = list(map(float, input().split()))
sum = 0
for i in range(0, n):
    d = num_list[i] % 10
    c = ((num_list[i] - d) / 10) % 10
    b = ((num_list[i] - 10 * c - d) / 100) % 10
    a = (num_list[i] - 100 * b - 10 * c - d) / 1000
    if(d - c - b - a > 0):
        sum += 1
print(sum)