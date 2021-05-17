a = list(map(int,input().split()))
b = []
for i in range(5):
    for j in range(5):
        for k in range(5):
            c = a[i] + a[j] + a[k]
            if i == j or i == k or j == k:
                continue
            else:
                if i < j < k:
                    b.append(c)
                else:
                    continue

sub = sorted(b)[-3]
print(sub)
