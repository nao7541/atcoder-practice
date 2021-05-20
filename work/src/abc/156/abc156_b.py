A, B= map(int, input().split())

for i in range(100000000000000000000):
    if B ** i > A:
        print(i)
        break

