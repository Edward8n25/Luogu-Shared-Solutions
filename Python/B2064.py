# B2064-斐波那契数列
k = int(input())
for i in range(1, k + 1):
    n = (int)(input())
    s = [0, 1, 1]
    for i in range(3, n + 1):
        s.insert(i, s[i - 1] + s[i - 2])
    print(s[n])