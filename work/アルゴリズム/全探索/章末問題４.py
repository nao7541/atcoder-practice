N = int(input())
a = list(map(int, input().split()))

sub = 0

for i in range(N):
    for j in range(N):
        if sub < a[i] - a[j]:
            sub = a[i] - a[j]

print(sub)