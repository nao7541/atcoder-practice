N = int(input())
A = []
#リストAにappend()を使って格納していく
for _ in range(N):
    A.append(input())

A = set(A)
print(len(A))