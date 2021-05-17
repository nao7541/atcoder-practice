N = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(len(p)-1):
    if p[i] == i+1:
        p[i], p[i+1] = p[i+1], p[i]
        ans += 1

if p[-1] == N:
    p[-2], p[-1] = p[-1], p[-2]
    ans += 1

print(ans)