N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N-2):
    for j in range(i+1, N):
        for k in range(j+1, N):
            maximam = max(max(L[i], L[j]), L[k])
            if (L[i]+L[j]+L[k])-2*maximam > 0:
                if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                    ans += 1

print(ans)
