N = int(input())
A = list(map(int, input().split()))
R = []
for i in range(N):
    R.append(A[i]%200)

# ここが重要
cnt = [0] * 200
ans = 0
for i in range(N):
    # この２行でi<jを満たすようにしている
    ans += cnt[R[i]]
    cnt[R[i]] += 1

print(ans)