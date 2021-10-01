N, K = map(int, input().split())
C = list(map(int, input().split()))
can = {}

for i in range(N):
    can.setdefault(C[i], 0)

# 種類
tmp  = 0
for i in range(K):
    if can[C[i]] == 0:
        tmp += 1
    can[C[i]] += 1

ans = tmp
for i in range(N-K):
    if can[C[i]] == 1:
        tmp -= 1
    can[C[i]] -= 1

    if can[C[i+K]] == 0:
        tmp += 1
    can[C[i+K]] += 1
    ans = max(ans, tmp)
    
print(ans)