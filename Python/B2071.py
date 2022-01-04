# B2071-余数相同问题
num_list = list(map(int, input().split()))
a = num_list[0]
b = num_list[1]
c = num_list[2]
for i in range(2, min(num_list)):
    if a % i == b % i == c % i:
        print(i)
        break
