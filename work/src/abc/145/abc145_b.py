N = int(input())
S = input()

if N % 2 != 0:
    print('No')
else:
    N_i = N // 2
    S_1 = S[:N_i]
    S_2 = S[N_i:]
    if S_1 == S_2:
        print('Yes')
    else:
        print('No')