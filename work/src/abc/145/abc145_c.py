import itertools
from math import sqrt
import numpy as np

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

li = []
for i in range(1, N+1):
    li.append(i)

ans = 0
cnt = 0
for i in itertools.permutations(li):
    tmp = 0
    for j in range(N-1):
        if np.sign(l[j][0]) == np.sign(l[j+1][0]):
            a = (l[i[j]-1][0] - l[i[j+1]-1][0]) ** 2
        else:
            a = (l[i[j]-1][0] + l[i[j+1]-1][0] * -1) ** 2
            
        if np.sign(l[j][1]) == np.sign(l[j+1][1]):
            b = (l[i[j]-1][1] - l[i[j+1]-1][1]) ** 2
        else:
            b = (l[i[j]-1][1] + l[i[j+1]-1][1] * -1) ** 2
        
        tmp += sqrt(a+b)
    ans += tmp
    cnt += 1

print(ans/cnt)