N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

must_ans = Q-K
d = {k: 0 for k in range(1,N+1)}
for a in A:
    d[a] += 1

for i in range(1, N+1):
    if d[i] <= must_ans:
        print('No')
    else:
        print('Yes')