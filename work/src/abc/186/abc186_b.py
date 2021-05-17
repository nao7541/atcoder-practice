import numpy as np
N, M = map(int,input().split()) 
a = [list(map(int, input().split())) for l in range(N)]

a_array = np.array(a)
num_min = np.amin(a_array)
ans = 0
for i in range(N):
    for j in range(M):
        ans += (a[i][j] - num_min)

print(ans)