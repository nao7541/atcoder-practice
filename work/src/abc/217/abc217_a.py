x, y = map(str, input().split())

for i in range(min(len(x), len(y))):
    if x[i] < y[i]:
        print('Yes')
        exit()
    elif x[i] > y[i]:
        print('No')
        exit()

if len(x) < len(y):
    print('Yes')
else:
    print('No')