from operator import mul
from functools import reduce
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

a = cmb(N, 2)

cnt = defaultdict(int)
for i in A:
    cnt[i] += 1

ans = 0
for k in cnt.keys():
    ans += cnt[k] * (cnt[k] -1) // 2

print(a-ans)