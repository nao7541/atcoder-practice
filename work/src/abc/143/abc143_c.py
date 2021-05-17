N = int(input())
S = input()
s_list = list(S)
ans = 0
mark = 2
for s in s_list:
    if s != mark:
        ans += 1
        mark = s

print(ans)
    