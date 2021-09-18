S = input()
X, Y = S[:-2], int(S[-1])

if Y <= 2:
    print(X + '-')
elif Y >= 7:
    print(X + '+')
else:
    print(X)