K, N= map(int, input().split())
A = list(map(int,input().split()))
A = list(sorted(set(A)))
ans = 1000000000000

for i in range(len(A)):
    if i == 0:
        tmp = A[N-1] - A[0]
    else:
        tmp = K - (A[i] - A[i-1])
    if tmp < ans:
            ans = tmp

print(ans)