from bisect import bisect_left
"""
二分探索法を用いて、「ペア和を最適化する問題」に対する全探索解法を高速化する
"""
inf = 200000000000

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 暫定最小値を格納する変数
min_value = inf
# bをソート
b.sort()

# aを固定して解く
for i in range(N):
    # bの中でK-a[i]以上の範囲での最小値を示すイテレータ
    ite = bisect_left(b, K-a[i])

    # イテレータの示す値を取り出す
    val = b[ite]

    # min_valueと比較する
    if a[i] + val < min_value:
        min_value = a[i] + val

print(min_value)