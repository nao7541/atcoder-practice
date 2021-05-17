a, b, c = map(int, input().split())
d = 100 -a
e = 100 -b
f = 100-c
ans = d*a/(a+b+c) + e*b/(a+b+c) + f*c/(a+b+c)

print(ans)