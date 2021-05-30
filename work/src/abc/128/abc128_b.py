N = int(input())
L = []
for i in range(N):
    a,b=input().split()
    L.append([a, int(b), i+1])
    
L = sorted(L, key=lambda x: (x[0], -x[1]))
for j in range(N):
    print(L[j][2])