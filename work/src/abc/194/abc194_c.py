from collections import Counter
N = int(input())
A = list(map(int, input().split()))
# 要素の数をカウントするときはCounterを使うと高速で数えられる
cnt = Counter(A)
""" ans = 0
for i in range(N):
    for j in range(i, N):
        ans += (A[i]-A[j])**2

print(ans) """
ans = 0
for j in range(-200, 201):
    # iとkが同じ時は差が0なので計算する必要がない
    for k in range(j+1, 201):
       ans += ((j-k)**2) * cnt[j] * cnt[k]

print(ans)

