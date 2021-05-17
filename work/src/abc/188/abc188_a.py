X,Y = map(int,input().split())

if X <= Y:
    print('Yes' if Y-X <= 2 else 'No')
else:
    print('Yes' if X-Y <= 2 else 'No')