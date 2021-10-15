import collections

N = int(input())
A = [input() for _ in range(N)]
A_count = collections.Counter(A)
A_max = max(A_count.values())

keys = [k for k, v in A_count.items() if v == A_max]
ans = sorted(keys)

for i in ans:
    print(i)
