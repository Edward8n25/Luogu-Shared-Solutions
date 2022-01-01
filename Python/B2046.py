# B2046-骑车与走路
x = float(input())
bike = 27 + 23 + x / 3.0
walk = x / 1.2
if bike > walk:
    print("Walk")
elif bike == walk:
    print("All")
elif bike < walk:
    print("Bike")