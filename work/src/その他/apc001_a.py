A,B = map(int,input().split())

if A == B:
    print(-1)
    exit()
elif B == 1:
    print(-1)
    exit()
elif A % B == 0:
    print(-1)
    exit()
for num in range(A, 10**18):
    if num % A ==0:
        if num % B !=0:
            print(num)
            exit()

print(-1)