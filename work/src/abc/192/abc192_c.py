N, K = map(int,input().split())

for i in range(K):
    g_1 = sorted(list(str(N)), reverse=True)
    g_1 = int(''.join(g_1))
    g_2 = sorted(list(str(N)))
    g_2 = int(''.join(g_2))
    N = g_1 - g_2
    

print(N)