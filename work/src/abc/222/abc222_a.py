N = input()
n = len(N)
if n == 1:
    print('000'+N)
elif n == 2:
    print('00'+N)
elif n == 3:
    print('0'+N)
else:
    print(N)