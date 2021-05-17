N = int(input())
memo = [-1] * (N+1)
def tribo(N):
    if N == 0:
        return 0
    if N == 1:
        return 0
    if N == 2:
        return 1
    
    if memo[N] != -1:
        return memo[N]
    
    memo[N] = tribo(N-1) + tribo(N-2) + tribo(N-3)
    return memo[N]

print(tribo(N))