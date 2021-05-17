N, X= map(int, input().split())
vp = [map(int, input().split()) for _ in range(N)]
v, p = [list(i) for i in zip(*vp)]
X *= 100
for i in range(N):
    X -= v[i]*p[i]
    if X < 0:
        print(i+1)
        exit()
print(-1)