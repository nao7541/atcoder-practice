N = int(input())
a = 0
b = 0
while N - 5**b > 0:
    c = N - 5**b
    for i in range(50):
        if c - 3**i == 0:
            a = i
            if a == 0 or b == 0:
                continue
            else:
                print(str(a)+ ' ' + str(b))
                exit()
    
    # N - 5**b
    b += 1

print(-1)
