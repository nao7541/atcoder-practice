N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

for i in range(N-2):
    if x[i] == y[i]:
        if x[i+1] == y[i+1]:
            if x[i+2] == y[i+2]:
                print('Yes')
                exit()

print('No')