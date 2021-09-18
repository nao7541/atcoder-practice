A, B, C, D = map(int, input().split())
E = 0
if B>=C*D:
    print(-1)
    exit()

for i in range(1, 100000000000):
    A += B
    E += C
    if A <= E*D:
        print(i)
        exit()