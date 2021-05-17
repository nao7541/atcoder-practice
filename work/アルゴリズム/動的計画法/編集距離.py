S = input()
T = input()

""" inf = 2000000000

dp = [[inf]*(len(S)+1) for j in range(len(T)+1)]

dp[0][0] = 0

for i in range(len(S)+1):
    for j in range(len(T)+1):
        # 変更操作
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                # 同じ文字の時はコストを増やさない
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                # 異なる場合、変更の処理を行うのでコストを1増やす
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        
        # 削除操作
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        
        # 挿入操作
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

print(dp[len(S)][len(T)]) """

def levenshtein(s1, s2):

    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                        dp[i][j - 1] + 1,         # deletion
                        dp[i - 1][j - 1] + cost)  # replacement

    return dp[n][m]

print(levenshtein(S,T))