N, A, X, Y = map(int, input().split())
if N > A:
    b = A*X
    c = N-A
    d = c*Y
    print(b+d)
else:
    b = N*X
    print(b)