import copy
num = int(input())
spot = list(map(int,input().split()))
b = []


c = 0
d = 0
for i in range(num):
    a = copy.copy(spot)
    a.pop(i)
    a.append(0)

    if i == 0:
        c += abs(a[i])
    else:
        if a[i] >= 0 and a[i-1] >= 0 or a[i] <= 0 and a[i-1] <= 0:
            d += abs(a[i-1] - a[i])
            c += d
        else:
            d += abs(a[i-1]) + abs(a[i])
            c += d
    d = 0
    #for j in range(num):
    #    if a[j] >= 0:
    #        c += a[j]
    #    else:
    #        c -= a[j]
    b.append(c)
    c = 0

for k in range(len(b)):
    print(b[k])
