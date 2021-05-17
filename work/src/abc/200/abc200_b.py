N,K = map(int,input().split())

for i in range(K):
    if N % 200 == 0:
        N =  N // 200
    else:
        s = str(N) + '200'
        N = int(s)

print(N)