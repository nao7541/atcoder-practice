import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
ans = 1000000000000000000000
for i in range(N+M):
    if len(A) == 0 or len(B) == 0:
        break
    dif = abs(A[-1] - B[-1])
    if ans > dif:
        ans = dif
    if A[-1] >= B[-1]:
        # popは末尾に対しては早いがそれ以外に対しては遅くなってしまう
        B.pop()
    elif A[-1] < B[-1]:
        A.pop()

print(ans)