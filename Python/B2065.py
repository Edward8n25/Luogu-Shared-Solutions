# B2065-鸡尾酒疗法
n = int(input())
list1 = list(map(int, input().split()))
x = list1[1] / list1[0]
for i in range(1, n):
    list2 = list(map(int, input().split()))
    y = list2[1] / list2[0]
    if (y - x) > 0.05:
        print("better")
    elif (x - y) > 0.05:
        print("worse")
    else:
        print("same")