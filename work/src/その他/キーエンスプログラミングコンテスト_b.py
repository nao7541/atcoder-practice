N,K = map(int,input().split())
a = list(map(int,input().split()))

a_max = max(a)
num_count = []
for i in range(a_max+1):
    c = a.count(i)
    num_count.append(c)

ans = 0
for k in range(K):
    p = 0
    for i in range(len(num_count)):
        if num_count[i] != 0:
            p += 1
            num_count[i] -= 1
        else:
            break
    
    ans += p

print(ans)