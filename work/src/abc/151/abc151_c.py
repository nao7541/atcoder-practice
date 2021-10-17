N, M = map(int, input().split())
xy = []
for i in range(M):
    a,b=input().split()
    xy.append([int(a), b])
if M == 0:
    print('0 0')
    exit()
p, s = [list(i) for i in zip(*xy)]

ac = []
for i,j in enumerate(s):
    if j == 'AC':
        ac.append(p[i])

ac = set(ac)
ac_ans = len(ac)
wa_ans = 0

ac_list = [0] * N
for i, j in enumerate(p):
    if s[i] == 'WA':
        if j in ac:
            if ac_list[j-1] == 0:
                wa_ans += 1
    if s[i] == 'AC':
        ac_list[j-1] = 1 

print(str(ac_ans)+ ' ' + str(wa_ans))