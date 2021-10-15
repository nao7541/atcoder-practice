N, M= map(int, input().split())
H = list(map(int, input().split()))

l = [list(map(int, input().split())) for l in range(M)]

ans = [1] * N
for i in range(M):
    a = l[i][0]
    b = l[i][1]
    if H[a-1] > H[b-1]:
        ans[b-1] = 0
    elif H[a-1] < H[b-1]:
        ans[a-1] = 0
    else:
        ans[b-1] = 0
        ans[a-1] = 0

print(ans.count(1))