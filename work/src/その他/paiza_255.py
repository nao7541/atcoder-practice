a = list(map(int,input().split()))
N = a[0]
X = a[1] # 走行距離
s = [input().split() for l in range(N)]
ans = []
for i in range(len(s)):
    if int(s[i][0]) > X:
        ans.append(int(s[i][1]))
    else:
        c = X - int(s[i][0]) # 走行距離から初乗り距離を引いた値
        d = int(s[i][1]) # 初乗り
        while c >= 0:
            c -= int(s[i][2])
            d += int(s[i][3])
        ans.append(d)

print(str(min(ans)) +' '+ str(max(ans)))