# B2053-求一元二次方程
a, b, c = map(float, input().split())
delta = (b ** 2 - 4 * a * c)
if delta < 0:
    print('No answer!')
elif delta == 0:
    aaaa = ((-b + delta ** 0.5) / (2 * a))
    print('x1=x2=' + '%.5f' % (aaaa))
elif delta > 0:
    aaaa = ((-b + delta ** 0.5) / (2 * a))
    bbbb = ((-b - delta ** 0.5) / (2 * a))
    if aaaa > bbbb:
        aaaa, bbbb = bbbb, aaaa
    print("x1=" + '%.5f' % (aaaa) + ";x2=" + '%.5f' % (bbbb))