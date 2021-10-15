N = int(input())
t = [0] * N
l = [0] * N
r = [0] * N
for i in range(N):
    #上から順番に代入していく
    t[i], l[i], r[i] = map(int, input().split())

ans = 0

""" for i in range(N-1):
    for j in range(i+1, N):
        if (l[j] >= l[i] and l[j] < r[i]) or (r[j] > l[i] and r[j] <= r[i]) or (l[i] >= l[j] and l[i] < r[j]) or (r[i] > l[j] and r[i] <= r[j]):
            ans += 1
        elif l[j] == r[i]:
            if (t[j] == 1 or t[j] == 2) and (t[i] == 1 or t[i] == 3):
                ans += 1
        elif r[j] == l[i]:
            if (t[j] == 1 or t[j] == 3) and (t[i] == 1 or t[i] == 2):
                ans += 1
        elif l[j] == l[i] and r[j] == r[i]:
            if (t[j] == 1 or t[j] == 2) and (t[i] == 1 or t[i] == 2):
                ans += 1
            elif (t[j] == 1 or t[j] == 3) and (t[i] == 1 or t[i] == 3):
                ans += 1

print(ans) """

# 上のやり方でも正解になるが、バグを埋め込んでしまう可能性が非常に高い(実際、3回ほどwaを出してしまった)
# そこで、初めに全ての区間を閉区間に直した上で計算するアルゴリズムを考える
# 今回、区間の両端点が整数であることから、tの値によって0.5を足し引きすることで閉区間を表現することができる

for i in range(N):
    if t[i] == 1:
        continue
    elif t[i] == 2:
        r[i] -= 0.5
    elif t[i] == 3:
        l[i] += 0.5
    elif t[i] == 4:
        r[i] -= 0.5
        l[i] += 0.5

for i in range(N-1):
    for j in range(i+1, N):
        if r[i] >= l[j] and r[j] >= l[i]:
            ans += 1

print(ans)