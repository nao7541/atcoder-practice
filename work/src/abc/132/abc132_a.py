S = input()

w1_cnt = S.count(S[0])
w2_cnt = 0
for i in range(1,len(S)):
    if S[0] != S[i]:
        w2_cnt += S.count(S[i])
        break

if w1_cnt == 2 and w2_cnt==2:
    print('Yes')
    exit()

print('No')