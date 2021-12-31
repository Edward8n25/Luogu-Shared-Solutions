# B2006-地球人口承载力估计
num_list = input().split()
x = int(num_list[0])
a = int(num_list[1])
y = int(num_list[2])
b = int(num_list[3])
solution = (a * x - b * y) / (a - b)
print("%.2f" % (solution))
