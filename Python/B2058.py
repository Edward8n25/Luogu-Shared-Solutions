# B2058-奥运奖牌计数
n = int(input())
# Gold-金牌 Silver-银牌 Copper-铜牌
Gold, Silver, Copper = 0, 0, 0
for i in range(0, n):
    num_list = list(map(int, input().split()))
    Gold += num_list[0]
    Silver += num_list[1]
    Copper += num_list[2]
print('%d %d %d %d' % (Gold, Silver, Copper, (Gold + Silver + Copper)))