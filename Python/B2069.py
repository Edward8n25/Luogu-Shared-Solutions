# B2069-求分数序列和
n = int(input())
p = [1]
q = [2]
sum = 0
# 先根据公式计算p和q的各项
for i in range(0, n - 1):
    q.append(p[i] + q[i])
    p.append(q[i])
# 将通项依次加起来
for i in range(0, n):
    sum += q[i] / p[i]
print("%.4f" % sum)