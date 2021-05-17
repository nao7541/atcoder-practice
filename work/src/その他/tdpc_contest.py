N = int(input())
a = list(map(int, input().split()))

dp = [[False]*(100*101) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j, dpj in enumerate(dp[i-1]):
        if dpj is True:
            dp[i][j] = True
            dp[i][j+a[i-1]] = True

ans = 0
for dpi in dp[N]:
    if dpi is True:
        ans += 1

print(ans)

