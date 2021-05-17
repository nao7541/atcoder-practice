N, K = map(int, input().split())
sub = 0
for i in range(N+1):
    for j in range(N+1):
        if 0 <= K - (i+j) <= N:
            sub += 1

print(sub)