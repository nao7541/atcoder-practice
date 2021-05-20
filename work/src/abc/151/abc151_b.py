N, K, M = map(int, input().split())
A = list(map(int, input().split()))

target = N*M
now = sum(A)
must = target - now
if must <= 0:
    print(0)
    exit()
if must <= K:
    print(must)
else:
    print(-1)