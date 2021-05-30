import math

N, D = map(int, input().split())
X = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        dim = 0
        if i >= j:
            continue
        for k in range(D):
            dim += (X[i][k] - X[j][k])**2
        dim = math.sqrt(dim)
        if dim.is_integer():
            ans += 1

print(ans)