# B2085-第 n 小的质数
# 检测是不是质数
def check(x):
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            return 0
    return 1
n = int(input())
i = 2
while True:
    n -= check(i)
    if not n:
        break
    i += 1
print(i)