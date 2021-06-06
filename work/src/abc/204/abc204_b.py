N = int(input())
l = list(map(int, input().split()))
ans = 0

for i in range(N):
    if l[i] <= 10:
        continue
    else:
        ans += l[i]-10

print(ans)