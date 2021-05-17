N = input()
N_reverse = N[::-1]
head_0 = 0
tail_0 = 0

if N == N[::-1]:
    print('Yes')
    exit()

for i in range(len(N)):
    if N[i] == '0':
        head_0 += 1
    else:
        break
for i in range(len(N_reverse)):
    if N_reverse[i] == '0':
        tail_0 += 1
    else:
        break
N = N[head_0:]
N = N[::-1]
N = N[tail_0:]
if N == N[::-1]:
    if head_0 <= tail_0:
        print('Yes')
    else:
        print('No')
else:
    print('No')