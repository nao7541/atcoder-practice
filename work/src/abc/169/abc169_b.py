N = int(input())
L = list(map(int,input().split()))
ans = L[0]
if 0 in L:
    print(0)
    exit()
for i in range(1,N):
    ans *= L[i]
    if ans > 10**18:
        print(-1)
        exit()

print(ans)
