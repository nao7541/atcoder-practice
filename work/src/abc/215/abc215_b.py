N = int(input())


for i in range(10000000000000000):
    now = 2**i
    if now > N:
        print(i-1)
        exit()

