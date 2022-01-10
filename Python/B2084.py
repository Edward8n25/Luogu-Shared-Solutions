# B2084-质因数分解
n = int(input())
# n是两个质数乘积，从头开始找到较小的质数，则另一个因数就是所求值
for i in range(2, n + 1):
    if n % i == 0:
        print(n // i)
        break