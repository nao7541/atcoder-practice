N = int(input())
A = list(map(int, input().split()))
A_sort = sorted(A, reverse=True)

booby = A_sort[1]

print(A.index(booby)+1)