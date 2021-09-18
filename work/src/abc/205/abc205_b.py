N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

N_list = []
for i in range(1, N+1):
    N_list.append(i)

if N_list == A:
    print('Yes')
else:
    print('No')

