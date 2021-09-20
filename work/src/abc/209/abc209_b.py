N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, N+1):
    a = A[i-1]
    if i % 2 == 0:
        a -= 1
    X -= a

if X >= 0:
    print('Yes')
else:
    print('No')