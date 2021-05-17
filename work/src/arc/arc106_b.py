N, M = map(int, input().split())
a = [list(map(int, input().split())) for l in range(N)]
b = [list(map(int, input().split())) for l in range(M)]

if sum(a[0]) != sum(a[1]):
    print("No")
    exit()

for i in range(len(a[0])):
    