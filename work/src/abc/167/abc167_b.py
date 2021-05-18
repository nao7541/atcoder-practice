A, B, C, K= map(int, input().split())
ans = 0
if A >= K:
    print(K)
    exit()
else:
    ans += A
    K -= A
K -= B
if K <= 0:
    print(ans)
    exit()
ans -= K
print(ans)