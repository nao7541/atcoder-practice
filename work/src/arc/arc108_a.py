S, P = map(int, input().split())
ans = 'No'

i = 1
while i*i <= P:
    if P % i == 0:
        j = P / i
        if i + j == S:
            ans = "Yes"
            break
    i += 1

print(ans)
