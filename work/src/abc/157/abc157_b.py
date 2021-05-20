a = [list(map(int, input().split())) for l in range(3)]
N = int(input())
b = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            a[i][j] = 0

for i in range(3):
    if a[i][0] == a[i][1] == a[i][2] or a[0][i] == a[1][i] == a[2][i]:
        print('Yes')
        exit()
 
if a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]: 
    print('Yes')
    exit()
print('No')
