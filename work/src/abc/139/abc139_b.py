A, B = map(int, input().split())
ans = 1
tap = A
if B == 1:
    print(0)
    exit()
elif A >= B:
    print(1)
    exit()

for i in range(10000000000):
    tap += (A-1)
    ans += 1
    if tap >= B:
        print(ans)
        exit()
