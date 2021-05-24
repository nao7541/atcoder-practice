N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
before_eat = -1
for i in range(N):
    eat = A[i]
    ans += B[eat-1]
    if eat-1 == before_eat:
        ans += C[eat-2]
    before_eat = A[i]

print(ans)
