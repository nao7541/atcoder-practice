N, M, L = map(int, input().split())
a = [list(map(int,input().split())) for i in range(N)]
b = [list(map(int,input().split())) for i in range(M)]
sub = [[0] * L for i in range(N)]

for i in range(N):
    for j in range(L):
        for k in range(M):
            sub[i][j] += a[i][k] * b[k][j]

for l in sub:
    print(*l)
