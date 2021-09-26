N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)
q, mod = divmod(X, sum_A)
for i in range(N):
    mod -= A[i]
    if mod < 0:
        a = i+1
        print(q*N+i+1)
        break