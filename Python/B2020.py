# B2020-分糖果
a, b, c, d, e = map(int, input().split())
s = sum([a, b, c, d, e])
# 第一个小朋友
a //= 3
b += a
e += a
# 第二个小朋友
b //= 3
a += b
c += b
# 第三个小朋友
c //= 3
b += c
d += c
# 第四个小朋友
d //= 3
c += d
e += d
# 第五个小朋友
e //= 3
d += e
a += e
print(a, b, c, d, e)
# 作差求得被吃掉的糖果
print(s-sum([a, b, c, d, e]))