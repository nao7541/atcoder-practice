import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0

# BとCの組み合わせを先に調べておく
BC_list = []
for c in range(N):
    b = B[C[c]-1]
    BC_list.append(b)

BC_list = collections.Counter(BC_list)

for i in range(N):
    ans += BC_list[A[i]]

print(ans)