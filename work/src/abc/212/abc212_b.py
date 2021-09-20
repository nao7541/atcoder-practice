X = input()

if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    print('Weak')
    exit()

for i in range(4):
    if i == 0:
        continue
    if X[i] != '0':
        if int(X[i]) != int(X[i-1]) + 1:
            print('Strong')
            exit()
    else:
        if int(X[i-1]) != 9:
            print('Strong')
            exit()

print('Weak')