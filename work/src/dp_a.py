N = int(input())
a = list(map(int,input().split()))
inf = 200000000

dp = [inf] * N

def chmin(a,b):
    if a > b:
        a = b

"""
もらう遷移形式
"""
# 初期条件
dp[0] = 0

for i in range(1,N):
    if i == 1:
        dp[i] = abs(a[i] - a[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(a[i] - a[i-1]),
                    dp[i-2] + abs(a[i] - a[i-2]))

print(dp[N-1])

"""
配る遷移形式
"""
dp = [inf] * N
# 初期条件
dp[0] = 0

for i in range(i):
    if i + 1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + abs(a[i] - a[i+1]))
    if i + 2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + abs(a[i] - a[i+2]))

print(dp[N-1])