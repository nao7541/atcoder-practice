N = input()
a = 0
for i in range(len(N)):
    a += int(N[i])

print('Yes' if a%9==0 else 'No')