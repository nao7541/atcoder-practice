N = int(input())
S = list(input())
Q = int(input())
T = [0] * Q
A = [0] * Q
B = [0] * Q
for i in range(Q):
    T[i], A[i], B[i] = map(int, input().split())

for i in range(Q):
    if T[i] == 1:
        S[A[i]-1], S[B[i]-1] = S[B[i]-1], S[A[i]-1]
    if T[i] == 2:
        S[:N], S[N:] = S[N:], S[:N]

print(''.join(S))