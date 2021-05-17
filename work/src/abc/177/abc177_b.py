S = input()
T = input()
ans = 10000
for i in range(len(S) - len(T) + 1):
    score = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            # 被りの個数
            score += 1
    # 変換する必要のある文字数に変換
    score = len(T)-score
    if score <= ans:
        ans = score

print(ans)