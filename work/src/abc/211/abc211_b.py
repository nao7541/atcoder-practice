A = []
for _ in range(4):
    A.append(input())

H_list = ['H', '2B', '3B', 'HR']

if set(H_list) <= set(A):
    print('Yes')
else:
    print('No')
    