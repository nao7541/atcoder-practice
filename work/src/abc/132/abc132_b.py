N = int(input())
P = list(map(int, input().split()))
ans = 0
for i in range(1, N-1):
    if max(P[i-1], max(P[i], P[i+1])) != P[i] and min(P[i-1], min(P[i], P[i+1])) != P[i]:
        ans += 1

print(ans)