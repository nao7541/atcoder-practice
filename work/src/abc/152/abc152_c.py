N = int(input())
P = list(map(int,input().split()))

ans = 1
tmp = P[0]

for i in range(1, N):
    if P[i] < tmp:
        ans += 1
        tmp = P[i]

print(ans)