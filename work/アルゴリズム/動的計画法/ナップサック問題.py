N, W = map(int, input().split())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0]*(W+1) for j in range(N+1)]
for i in range(N):
    for w in range(W+1):
        # i番目の品物を選ぶ場合
        if w - weight[i] >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-weight[i]] + value[i])

        # i番目の品物を選ばない場合
        dp[i+1][w] = max(dp[i+1][w], dp[i][w])

# 最適値の出力
print(dp[N][W])