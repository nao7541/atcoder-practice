N = int(input())
A = list(map(int, input().split()))
A_rev = 0

for i in range(N):
    A_rev += 1/A[i]

ans = 1/A_rev
print(ans)