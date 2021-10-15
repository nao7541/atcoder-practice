N = int(input())
A = list(map(int, input().split()))
b = []
for i in range(N):
   if A[i] % 2 == 0:
       b.append(A[i])

for j in range(len(b)):
    if b[j] % 3 == 0 or b[j] % 5 == 0:
        continue
    else:
        print('DENIED')
        exit()

print('APPROVED')