N = int(input())
ans = ''
for i in range(1000000000000000):
    if N == 1:
        ans += 'A'
        break
    elif N % 2 == 0:
        N //= 2
        ans += 'B'
    else:
        N -= 1
        ans += 'A'

print(ans[::-1])