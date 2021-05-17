a = int(input())
sub = 0


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return len(lower_divisors) + len(upper_divisors)

for i in range(1,a+1,2):
    # num_divisors_trial_division(i)
    if make_divisors(i) == 8:
        sub += 1

print(sub)