N = int(input())
A = list(map(int, input().split()))
a_half = (2**N) // 2
A_1 = max(A[:a_half])
A_2 = max(A[a_half:])
second = min(A_1, A_2)
print(A.index(second)+1)