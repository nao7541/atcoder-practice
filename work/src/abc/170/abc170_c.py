X, N = map(int, input().split())
A = list(map(int, input().split()))
p = list(range(200, -200, -1))


for i in range(N):
    p.remove(A[i])

ans = 100000000000
div = 100000000000
for j in range(len(p)):
    if abs(p[j] - X) <= div:
        div = abs(p[j] - X)
        ans = p[j]

print(ans) 
