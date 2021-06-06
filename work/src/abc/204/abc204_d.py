N = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
oven_1 = l[0]
oven_2 = l[1]
for i in range(2,N):
    if oven_1 > oven_2:
        oven_2 += l[i]
    else:
        oven_1 += l[i]
    
print(max(oven_1, oven_2))