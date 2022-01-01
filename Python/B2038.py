# B2038-奇偶 ASCII 值判断
n = input()
asc = ord(n)
if asc % 2 == 0:
    print("NO")
elif asc % 2 != 0:
    print("YES")