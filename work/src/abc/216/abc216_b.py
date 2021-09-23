N = int(input())
xy = [map(str, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
for i in range(N):
    for j in range(i+1, N):
        if x[i] == x[j] and y[i] == y[j]:
            print('Yes')
            exit()

print('No')
