H, W, X, Y= map(int, input().split())
a = [input().split() for l in range(H)]
# 文字列を１文字ずつの要素に分割する
a_list= [list(x[0]) for x in a]
ans = 0
#print(a)
if a_list[X-1][Y-1] == '#':
    print(0)
    exit()
for i in range(Y-2, -1, -1):
    if a_list[X-1][i] == '.':
        ans += 1
    else:
        break
for i in range(Y, W):
    if a_list[X-1][i] == '.':
        ans += 1
    else:
        break
for i in range(X-2, -1, -1):
    if a_list[i][Y-1] == '.':
        ans += 1
    else:
        break
for i in range(X, H):
    if a_list[i][Y-1] == '.':
        ans += 1
    else:
        break
print(ans+1)
