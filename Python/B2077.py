# B2077-角谷猜想
N = int(input())
while N != 1:
    if N % 2 == 1:
        print(str(N) + "*3+1=" + str(N * 3 + 1))
        N = N * 3 + 1
    elif N % 2 == 0:
        print(str(N) + "/2=" + str(N // 2))
        N = N // 2
print("End")
