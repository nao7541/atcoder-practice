N = int(input())
X = list(map(int,input().split()))

a = len(X)
b = len(set(X))

if a == b:
    print('YES')
else:
    print('NO')