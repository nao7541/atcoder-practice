N = int(input())

for i in range(1, 10):
    a = N / i
    if a.is_integer():
        if a <= 9:
            print('Yes')
            exit()
print('No')