total = 0
sub = []
while True:
    A,B = map(int,input().split())
    if A == B == 0:
        break
    for i in range(1,A+1):
        for j in range(1,A+1):
            for k in range(1,A+1):
                if i + j + k == B:
                    if i == j or i == k or j == k:
                        continue
                    elif i > j > k:
                        total += 1
                    else:
                        continue
    sub.append(total)
    total = 0
for i in range(len(sub)):
    print(sub[i])