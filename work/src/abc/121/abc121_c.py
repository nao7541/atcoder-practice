
N, M = map(int, input().split())
P = [list(map(int,input().split())) for i in range(N)]
a = 0

p_sort = sorted(P)

for i in range(N):
    if M - p_sort[i][1] >= 0:
        a += p_sort[i][0] * p_sort[i][1]
        M -= p_sort[i][1]
    else:
        a += M * p_sort[i][0]
        print(a)
        exit()

print(a)


# print(p_sort)