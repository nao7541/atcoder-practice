import math
N = int(input())
x = N * 1.08
x = math.floor(x)

if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
else:
    print(':(')

