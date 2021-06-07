from itertools import combinations

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

for comb in combinations(l, 3):
    x1, y1 = comb[0]
    x2, y2 = comb[1]
    x3, y3 = comb[2]
    x1 -= x3
    y1 -= y3
    x2 -= x3
    y2 -= y3
    if x2*y1 == x1*y2:
        print('Yes')
        exit()
    
print('No')