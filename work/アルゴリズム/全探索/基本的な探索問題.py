"""
N個の整数(a,a1,...)と整数値vが与えられたときに、ai = vとなるデータが存在するか判定する
"""

N, v = map(int, input().split())
a = list(map(int, input().split()))

# 初めはFalseに設定する
exist = False
for i in range(N):
    if a[i] == v:
        exist = True

print(exist)

# 計算量はN個の値を順に調べているのでO(N)となる

"""
次に条件を満たす添え字iを表示させるようにする
"""
found_id = -1 # 初期値はあり得ない値にしておく

for i in range(N):
    if a[i] == v:
        found_id = i
        break

print(found_id)

"""
数列の最小値を求める
"""
min_value = 2000000000000 # 十分大きな値に設定

for i in range(N):
    if a[i] < min_value:
        min_value = a[i]

print(min_value)

"""
N個の整数(a,a1,...)と整数値vが与えられたときに、ai = vとなるデータがいくつ存在するか
"""
c = 0

for i in range(N):
    if a[i] == v:
        c += 1

print(c)