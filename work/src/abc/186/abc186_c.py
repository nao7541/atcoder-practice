N = int(input())
ans = 0
for i in range(1, N+1):
    if '7' in str(i):
        continue
    else:
        a = oct(i)[2:]
        if '7' in str(a):
            continue
        ans += 1

print(ans)