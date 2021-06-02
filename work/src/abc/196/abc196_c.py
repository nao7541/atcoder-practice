N = int(input())
ans = 0

for i in range(1, 10000000):
    a = int(str(i)+str(i))
    if a <= N:
        ans += 1
    else:
        break

print(ans)