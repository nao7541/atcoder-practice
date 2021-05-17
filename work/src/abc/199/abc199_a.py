l = list(map(int, input().split()))
a = l[0] ** 2
b = l[1] ** 2
c = l[2] ** 2

if a + b < c:
    print('Yes')
else:
    print('No')