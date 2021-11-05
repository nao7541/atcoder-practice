N = int(input())
A = list(map(int, input().split()))
li = []
for i,j in enumerate(A):
    li.append([j, i+1])

li = sorted(li)
ans = []
for i in li:
    ans.append(i[1])

print(' '.join(map(str, ans)))