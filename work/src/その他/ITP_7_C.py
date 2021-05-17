a = list(map(int,input().split()))
b = [input().split() for l in range(a[0])]

for i in range(a[0]):
    b_row = b[i]
    b_int = [int(s) for s in b_row]
    b_int.append(sum(b_int))
    b[i] = b_int

c = []
d = 0
for j in range(len(b[0])):
    for k in range(a[0]):
        d += b[k][j]
    c.append(d)
    d = 0

b.append(c)
# 二次元配列を次元ごとに要素を出力する
for l in b:
    print(*l)
