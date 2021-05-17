N = int(input())

a = N // 100
if N % 100 == 0:
    print(a)
else:
    print(a+1)