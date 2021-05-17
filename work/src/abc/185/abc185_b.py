N, M, T= map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
a,b = [list(i) for i in zip(*ab)]

now_battery = N - a[0]
if now_battery <= 0:
    print('No')
    exit()
for i in range(M):
    now_battery = min(N, now_battery+(b[i]-a[i]))
    if i == M-1:
        break
    now_battery -= (a[i+1] - b[i])
    if now_battery <= 0:
        print('No')
        exit()
now_battery -= (T-b[M-1])
print('Yes' if now_battery > 0 else 'No')