N, X, T= map(int, input().split())

if N % X == 0:
    a = N // X
else:
    a = (N // X) + 1
print(a*T)