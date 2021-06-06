from itertools import combinations

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

for comb in combinations(l, 3):
    x_max = max(comb[0][0], max(comb[1][0], comb[2][0]))
    x_min = min(comb[0][0], min(comb[1][0], comb[2][0]))
    y_max = max(comb[0][1], max(comb[1][1], comb[2][1]))
    y_min = min(comb[0][1], min(comb[1][1], comb[2][1]))    
    
    print(comb)