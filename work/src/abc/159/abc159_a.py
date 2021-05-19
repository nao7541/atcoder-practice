import math
N, M= map(int, input().split())

def combinations_count(n, r):
    if n == 0 or n == 1:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans_1 = combinations_count(N, 2)
ans_2 = combinations_count(M, 2)

print(ans_1+ans_2)