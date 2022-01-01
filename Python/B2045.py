# B2045-晶晶赴约会
x = int(input())
if x == 1 or x == 3 or x == 5:
    print("NO")
# 避免错误数据的干扰
elif x > 7 or x <= 0:
    print("NO")
else:
    print("YES")