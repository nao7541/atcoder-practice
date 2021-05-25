N = int(input())
ans = 0

if N < 10:
    ans += N
elif N < 100:
    ans += 9
elif N < 1000:
    ans += 9 + (N-99)
elif N < 10000:
    ans += 9 + 900
elif N < 100000:
    ans += 909 + (N-9999)
elif N == 100000:
    ans += 909 + (N-9999)-1
print(ans)
