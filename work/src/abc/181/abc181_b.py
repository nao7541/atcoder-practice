N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
ans = 0
for i in range(N):
    a = y[i] * (y[i]+1) // 2
    b = (x[i]-1)* x[i] // 2
    ans += a-b
    
print(ans)