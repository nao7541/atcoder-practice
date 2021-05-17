a, b = map(int, input().split())
c, d = map(int, input().split())
ans = 0
if a==c and b==d:
    print(0)
    exit
e = min(abs(a-c), abs(b-d))
if a < c:
    a += e
else:
    a -= e
if b < d:
    b += e
else:
    b -= e
while a+b != c+d or a-b != c-d or abs(a-c)+abs(b-d)>3:
    k = 0
    f = a+3
    g = a-3
    h = b+3
    i = b-3