import math

# ２点間の距離を求める関数
def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

# 求める値を、十分大きい値で初期化
minimum_dist = 100000000

for i in range(N):
    for j in range(i+1, N):
        dist_i_j = calc_dist(x[i], y[i], x[j], y[j])

        # 暫定最小値をdist_i_jと比べる
        if dist_i_j < minimum_dist:
            minimum_dist = dist_i_j

print(minimum_dist)