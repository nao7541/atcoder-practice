P = list(map(int, input().split()))
alp = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in range(len(P)):
    ans += alp[P[i]-1]

print(ans)