N = int(input())
""" num_divi = []
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors + upper_divisors[::-1])

for i in range(1, N):
    num_divi.append(make_divisors(i))

print(sum(num_divi)) """

ans = 0

for a in range(1, N):
    for b in range(1, N):
        c = N - a*b
        if c <= 0:
            break
        ans += 1

print(ans)