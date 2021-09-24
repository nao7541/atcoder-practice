N = int(input())
P = list(map(int, input().split()))
""" Q = []

a = []
for i, j in enumerate(P):
    a.append([i, j])

a = sorted(a, key=lambda x: x[1])  #[1]に注目してソート
for i in a:
    Q.append(str(i[0]+1))


ans = " ".join(Q)
print(ans) """

# これでも正解ではあるが、3行目のQを定義する際に、空の状態で生成するのではなく、-1を使って長さをNにすることでもっと楽に解くことができる

Q = [-1]*N
for i in range(1,N+1):
    Q[P[i-1]-1] = i

ans = " ".join(map(str, Q))
print(ans)