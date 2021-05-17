inf = 200000000000000000000000000000000

N = int(input())

xy = [map(int, input().split()) for _ in range(N)]
h, s = [list(i) for i in zip(*xy)]

# 2分探索
left = 0
right = inf

while right - left > 1:
    mid = (left + right) // 2

    # 判定
    ok = True
    t = [0] * N # 各風船を割るまでの時間制限
    for i in range(N):
        # そもそもmidが初期高度より低かったらfalse
        if mid < h[i]:
            ok = False
        else:
            t[i] = (mid - h[i]) // s[i]
    # 時間制限が差し迫っている順にソート
    t.sort()
    for i in range(N):
        if t[i] < i:
            ok = False # 時間切れの発生
        
    if ok:
        right = mid
    else:
        left = mid

print(right)
