from collections import Counter
N = int(input())
a = [input() for i in range(N)]
a = list(set(a))
N = len(a)
for i in range(N):
    if '!' in a[i]:
        b = a[i]
        a[i] = b[1:]

a_i = Counter(a)
key = [k for k, v in a_i.items() if v >= 2]
if key == []:
    print('satisfiable')
else:
    print(key[0])
