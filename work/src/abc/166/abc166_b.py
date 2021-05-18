N, K= map(int, input().split())
ans = list(range(1, N+1))

for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    have = []
    for j in ans:
        if j in A:
            have.append(j)
    for k in have:
        ans.remove(k)

print(len(ans))