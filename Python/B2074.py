# B2074-计算星期几
a, b = map(int, input().split())
num = (a ** b) % 7
if num == 0:
    print("Sunday")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")