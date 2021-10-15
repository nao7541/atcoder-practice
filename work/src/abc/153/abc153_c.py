N, K= map(int, input().split())
H = list(map(int,input().split()))
H = sorted(H)

if K >= N:
    print(0)
    exit()
else:
    for i in range(K):
        H.pop()
    print(sum(H))