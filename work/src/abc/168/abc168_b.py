num = int(input())
a = input()

if len(a) <= num:
    print(a)
else:
    b = a[:num] + '...'
    print(b)
