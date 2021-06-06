x, y = map(int, input().split())
l = [0, 1, 2]
if x == y:
    print(x)
    exit
else:
    l.remove(x)
    l.remove(y)
    print(l[0])
    