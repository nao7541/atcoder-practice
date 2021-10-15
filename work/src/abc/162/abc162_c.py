import math
N = int(input())
ans = 0
tmp = {}
for i in range(1, N+1):
    tmp.setdefault(i, 0)


for i in range(1, N+1):
    for j in range(1, N+1):
        tmp[math.gcd(i,j)] += 1
        
for i in range(1, N+1):
    for j in range(1, len(tmp)+1):
        a = math.gcd(i, j)
        ans += a*tmp[j]

print(ans)