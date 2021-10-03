import itertools

N = input()
N = list(N)
num = len(N) // 2
p = list(itertools.permutations(N))
ans = 0
for i in range(len(p)):
    a = int(''.join(p[i][:num]))
    b = int(''.join(p[i][num:]))
    a *= b
    if ans < a:
        ans = a

print(ans)