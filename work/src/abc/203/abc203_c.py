""" import numpy as np

N, K = map(int, input().split())
friends = [list(map(int, input().split())) for l in range(N)]
friends = np.array(friends)
ans = 0
ans += K
before_place = 0
b = 0
for i in range(N):
    # 友達に会えるかどうか
    # 辿り着いた村までに友達がいるか
    a = friends[friends[:,0] <= ans]
    # すでにお金をもらっている場合は消す
    a = a[before_place < a[:, 0]]
    a = np.sum(a, axis=0)
    # もらえるお金
    a = a[1]
    # お金が貰えなかったら進めない
    if a == 0:
        break
    # お金をもらっていたらその分進める
    ans += a
    # 進む前にいた場所をメモする
    if i == 0:
        before_place += K
        b = a
        continue
    # 前回の進んだ距離をメモ
    before_place += b
    # 進んだ距離を更新する
    b = a

print(ans) """

# 回答
N, K = map(int, input().split())
mat = []

for _ in range(N):
    a, b = map(int, input().split())
    mat.append((a, b))

mat.sort() # aを小さい順にソートする
now = K # 初めの所持金でKまで進めることができる

for i in range(N):
    a, b = mat[i]
    if now >= a:
        # 村A_iの人がB_i円くれるので、すぐに使ってB_i進む
        now += b
    else:
        break
print(now)
