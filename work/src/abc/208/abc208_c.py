N, K = map(int, input().split())
a = list(map(int, input().split()))

ans_1 = K // N
now = K - N*ans_1

b = []
for i, j in enumerate(a):
    b.append([i, j])

# idが小さい順に並んでいて、かつ元の並び順も保存してある
b = sorted(b, key=lambda x: x[1])
        
ans = [-1]*N
for i in range(N):
    if now > 0:
        ans[b[i][0]] = ans_1 + 1
        now -= 1
    else:
        ans[b[i][0]] = ans_1

for i in ans:
    print(i)