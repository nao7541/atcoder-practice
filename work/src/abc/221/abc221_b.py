S = input()
T = input()
s = list(S)

if S == T:
    print('Yes')
    exit()

for i in range(len(S)-1):
    if S[i] == T[i+1] and S[i+1] == T[i]:
        s[i], s[i+1] = s[i+1], s[i]
        if s == list(T):
            print('Yes')
            exit()

print('No')