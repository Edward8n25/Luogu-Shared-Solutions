# B2042-判断一个数能否同时被 3 和 5 整除
x = int(input())
if x % 3 == 0 and x % 5 == 0:
    print("YES")
else:
    print("NO")