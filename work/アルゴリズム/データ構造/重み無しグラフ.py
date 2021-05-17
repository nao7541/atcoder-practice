n, m = map(int, input().split())
p = []
for i in range(m-1):
    p.append(list(map(int, input().split())))

print(p)

l = [[] for i in range(n)]
for pi in p:  #0-originedに注意
    l[pi[0]].append(pi[1])
    l[pi[1]].append(pi[0])
print(l)