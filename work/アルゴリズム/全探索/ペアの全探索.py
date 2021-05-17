"""
N個の整数a0,a1...と、N個の整数b0,b1...が与えられる。2組の整数列からそれぞれ1個ずつ整数を選んで和をとり、
その和として考えられる値のうち、整数K以上の範囲内での最小値を求める
"""

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_value = 2000000000000

for i in range(N):
    for j in range(N):
        # 和がK未満の場合は切り捨て
        if a[i] + b[j] < K:
            continue
        # 最小値の場合は更新
        if a[i] + b[j] < min_value:
            min_value = a[i] + b[j]

print(min_value)

# 考えられる場合の数はN**2通りであるから、計算量はO(N**2)となる
# 二分探索法を用いることでもっと減らすことができる