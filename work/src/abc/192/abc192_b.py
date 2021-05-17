S = input()
ans = 'Yes'
for i in range(len(S)):
    if i % 2 == 0:
        if S[i].islower():
            continue
        else:
            ans = 'No'
            break
    else:
        if S[i].isupper():
            continue
        else:
            ans = 'No'
            break
print(ans)
            
        