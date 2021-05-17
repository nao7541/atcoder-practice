N = int(input())
s = [input() for i in range(N)]

for i in range(len(s)):
    if s[i][-1] == 's' or s[i][-1] == 'o' or s[i][-1] == 'x':
        s[i] += 'es'

    elif s[i][-2:] == 'sh' or s[i][-2:] == 'ch':
        s[i] += 'es'
    
    elif s[i][-1] == 'f':
        s[i] = s[i].strip('f')
        s[i] += 'ves'
    
    elif s[i][-2:] == 'fe':
        s[i] = s[i].strip('fe')
        s[i] += 'ves'
    
    elif s[i][-1] == 'y':
        if s[i][-2] != 'a' and s[i][-2] != 'i' and s[i][-2] != 'u' and s[i][-2] != 'e' and s[i][-2] != 'o':
            s[i] = s[i].strip('y')
            s[i] += 'ies'
        else:
            s[i] += 's'
    else:
        s[i] += 's'
    
    print(s[i])