P = int(input())
n = 0
high = 1*2*3*4*5*6*7*8*9*10

for i in range(10, 0, -1):
    a = P// high
    n += a    
    P -= high*a
    high /= i
    if P <= 0:
        break

print(int(n))