S = input()
S_rev = S[::-1]
if len(S) % 2 == 0:
    N = (len(S)//2)
else:
    N = (len(S) // 2) + 1
ans = 0
for i in range(N):
    if S[i] != S_rev[i]:
        ans += 1

print(ans)