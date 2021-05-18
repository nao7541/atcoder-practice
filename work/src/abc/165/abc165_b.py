N = int(input())
now = 100
for i in range(1,1000000000000000000):
    now += (now//100)
    if now >= N:
        print(i)
        exit()
    