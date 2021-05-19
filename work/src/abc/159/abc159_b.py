S = input()
N = len(S)
N_1 = (N-1)//2
N_2 = (N+3)//2-1
S_1 = S[:N_1]
S_2 = S[N_2:]
if S_1 == S_1[::-1] and S_2 == S_2[::-1] and S == S[::-1]:
    print('Yes')
else:
    print('No')