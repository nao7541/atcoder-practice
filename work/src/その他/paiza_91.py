N = int(input())
s = [input().split() for l in range(N)]

a = 0
b = 0

for i in range(len(s)):
    if s[i][0] == 'SET':
        if s[i][1] == '1':
            a = int(s[i][2])
        if s[i][1] == '2':
            b = int(s[i][2])
    if s[i][0] == 'ADD':
        c = a + int(s[i][1])
        b = c
    if s[i][0] == 'SUB':
        c = a - int(s[i][1])
        b = c

print(str(a) + ' '+ str(b))