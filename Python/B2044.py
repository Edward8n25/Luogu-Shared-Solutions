# B2044-有一门课不及格的学生
list = input().split()
chinese = int(list[0])
math = int(list[1])
english = int(list[2])
if chinese < 60 and math >= 60 and english >= 60:
    print("1")
elif chinese >= 60 and math < 60 and english >= 60:
    print("1")
elif chinese >= 60 and math >= 60 and english < 60:
    print("1")
else:
    print("0")