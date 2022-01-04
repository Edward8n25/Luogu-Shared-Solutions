# B2073-求小数的某一位
a, b, n = map(int, input().split())
print(a * (10 ** 10000) // b // (10 ** (10000 - n)) % 10)