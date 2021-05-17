N = int(input())
a = list(map(int,input().split()))
ans = 0
gcd_max = 0
for i in range(2, max(a)+1):
    gcd = 0
    for j in range(N):
        if a[j] % i == 0:
            gcd += 1
    
    if gcd >= gcd_max:
        gcd_max = gcd
        ans = i
print(ans)