N = int(input())
A = list(map(int, input().split()))
A_sort = sorted(A)
diff = 0
for i in range(N):
    if A[i] != A_sort[i]:
        diff += 1

if diff <= 2:
    print('YES')
else:
    print('NO')