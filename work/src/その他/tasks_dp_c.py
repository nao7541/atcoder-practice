a = int(input())

xyz = [map(int, input().split()) for _ in range(a)]
x, y, z = [list(i) for i in zip(*xyz)]

dp = [[0]*(a+1) for j in range(3)]

dp[0][0] = x[0]
dp[1][0] = y[0]
dp[2][0] = z[0]

for i in range(1, a):
    dp[0][i] = max(dp[1][i-1]+x[i], dp[2][i-1]+x[i])
    dp[1][i] = max(dp[0][i-1]+y[i], dp[2][i-1]+y[i])
    dp[2][i] = max(dp[0][i-1]+z[i], dp[1][i-1]+z[i])

print(max(dp[0][a-1], max(dp[1][a-1], dp[2][a-1])))
