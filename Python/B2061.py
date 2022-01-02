# B2061-整数的个数
k = int(input())
num_1 = 0
num_5 = 0
num_10 = 0
num_list = list(map(int, input().split()))
for i in range(0, k):
    if num_list[i] == 1:
        num_1 += 1
    elif num_list[i] == 5:
        num_5 += 1
    elif num_list[i] == 10:
        num_10 += 1
print(num_1)
print(num_5)
print(num_10)