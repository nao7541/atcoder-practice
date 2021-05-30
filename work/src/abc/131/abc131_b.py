N, L = map(int, input().split())
apple_list = list(range(1, N+1))
for i in range(N):
    apple_list[i] += (L-1)

apple_all = sum(apple_list)
div = 20000000000000
for j in range(N):
    d = apple_all - apple_list[j]
    if div > abs(apple_all-d):
        div = abs(apple_all-d)
        ans = d

print(ans)