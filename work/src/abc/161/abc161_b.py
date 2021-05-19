N, M= map(int, input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
total_vote = sum(A)
for i in range(M):
    if A[i] >= (total_vote / (4*M)):
        continue
    else:
        print('No')
        exit()

print('Yes')