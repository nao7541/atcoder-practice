N, S, D= map(int, input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
for i in range(N):
    if x[i] < S:
        if y[i] > D:
            print('Yes')
            exit()
print('No')