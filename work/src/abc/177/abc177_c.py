N = int(input())
l = list(map(int, input().split()))
su = sum(l)
ans = 0

for i in range(N-1):
    su -= l[i]
    ans += l[i]*su

if ans >= 10**9 + 7:
    print(ans%(10**9+7))
else:
    print(ans)