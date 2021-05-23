N = int(input())
S = input()
ans = ''
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(S)):
    W = S[i]
    ans += alp[alp.find(W)+N]

print(ans)