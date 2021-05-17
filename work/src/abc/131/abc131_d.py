import operator
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]
l = sorted(l, key=operator.itemgetter(1))

res = 0
current_end_time = 0
for i in range(N):
    if l[i][1] - current_end_time < l[i][0]:
        continue
    res += 1
    current_end_time += l[i][0]

if res == N:
    print('Yes')
else:
    print('No')