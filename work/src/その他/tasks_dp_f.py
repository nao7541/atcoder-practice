s = input()
t = input()

n, m = len(s), len(t)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

length = dp[n][m]
ans = [ [] for i in range(length) ]
n -=1
m -=1
while length>0:
    if s[n] == t[m]:
        ans[length-1] = s[n]
        n -= 1
        m -= 1
        length -= 1
    elif dp[n][m] == dp[n-1][m]:
        n -= 1
    else:
        m -= 1

print(''.join(ans))

