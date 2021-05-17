N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
ans = 0
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        x_div = x[j] - x[i]
        y_div = y[j] - y[i]
        if y_div / x_div <= 1 and y_div / x_div >= -1:
            ans += 1

print(ans)