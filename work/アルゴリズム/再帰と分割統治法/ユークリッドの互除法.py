"""
ユークリッドの互除法を使って最大公約数を求める
"""
N, K = map(int, input().split())

def GCD(m, n):
    if n == 0:
        return m
    return GCD(n, m%n)

print(GCD(N,K))