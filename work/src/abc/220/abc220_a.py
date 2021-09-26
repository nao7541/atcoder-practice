A, B, C = map(int, input().split())
d = C
for i in range(1, 10000):
    if C > B:
        print(-1)
        exit()
    elif A <= C and C <= B:
        print(C)
        exit()
    C += d 