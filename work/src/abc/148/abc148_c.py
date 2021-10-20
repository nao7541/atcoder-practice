A, B = map(int, input().split())

num_max = max(A, B)
num_min = min(A, B)

for i in range(1,300000):
    a = num_max * i
    if a % num_min == 0:
        print(a)
        break
