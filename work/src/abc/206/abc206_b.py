N = int(input())
bank = 0

for i in range(1, 1000000000000):
    bank += i
    if bank >= N:
        print(i)
        exit()