N = int(input())
a = list(map(int, input().split()))

min_value = 1000000000
second_value = 1000000000

for i in range(N):
    if a[i] < min_value:
        second_value = min_value
        min_value = a[i]
    elif a[i] < second_value:
        second_value = a[i]

print(second_value)