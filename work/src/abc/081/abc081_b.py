N = int(input())
a = list(map(int, input().split()))
b = 0
sub = 0

def calc(n):
    return n / 2

for i in range(N):
    if a[i] % 2 == 0:
        b += 1

while b == N:
    a = list(map(calc, a))
    sub += 1
    b = 0
    for i in range(N):
        if a[i] % 2 == 0:
            b += 1

print(sub)