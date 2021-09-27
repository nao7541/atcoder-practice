# 組み合わせの総数を出力
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

a = cmb(3, 2)
print(a)

# 同じ値になる組み合わせ
""" from collections import defaultdict

cnt = defaultdict(int)
for li in l:
  cnt[li] += 1
 
ans = 0  
for k in cnt.keys():
  ans += cnt[k] * (cnt[k] - 1) // 2 """