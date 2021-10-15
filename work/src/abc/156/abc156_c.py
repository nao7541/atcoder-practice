N = int(input())
X = list(map(int,input().split()))

hp = 10000000000000000000000

for i in range(1, 101):
    tmp = 0
    for j in range(N):
        tmp += (X[j] - i) ** 2
    
    if tmp < hp:
        hp = tmp

print(hp)        