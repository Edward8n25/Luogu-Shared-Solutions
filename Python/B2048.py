# B2048-计算邮资
list = input().split()
x = int(list[0])
C = list[1]
gold = 0
if x <= 1000:
    gold += 8
elif x > 1000:
    gold += 8
    x -= 1000
    gold += x // 500 * 4
    if x % 500 != 0:
        gold += 4
if C == 'y':
    gold += 5
print(gold)