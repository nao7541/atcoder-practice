import numpy as np
N, M = map(int, input().split())
l = [list(map(int, input().split())) for l in range(M)]
road = [[] for i in range(N)]
ans = N

#print(road)
for i in range(M):
    prev = l[i][0] - 1
    road[prev].append(l[i][1])
    
can_go = []
already_visited = []
for j in range(N):
    can_go.append(road[j])
    
    already_visited.append(j+1)
    


print(road)
    

