import math
N = int(input())
a = math.sqrt(N)
a = math.floor(a)

ans = []
for i in range(2, a+1):
    for k in range(2, 35):
        if i ** k <= N:
            num = math.sqrt(i)
            ans.append([i,k])
        else:
            break
ans_ = []
for i in range(len(ans)):
    p = ans[i][0] ** ans[i][1]
    ans_.append(p)

n = list(set(ans_))

print(N - len(n))