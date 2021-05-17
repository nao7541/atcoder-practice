N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
x = x[::-1]
y = y[::-1]

def calc_plus(n):
    return
a = 0
t = 0
ans = 0
for i in range(N):
    x[i] += t
    if x[i] % y[i] == 0:
        continue
    else:
        a = y[i] - (x[i]%y[i])
        ans += a
        t += y[i] - (x[i]%y[i])

print(ans)

