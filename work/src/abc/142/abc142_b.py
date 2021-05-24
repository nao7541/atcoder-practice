A, B = map(int, input().split())
l = list(map(int, input().split()))
ans = 0

for i in range(A):
    if l[i] >= B:
        ans += 1

print(ans)