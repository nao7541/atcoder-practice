A, B, C = map(int, input().split())
A_list = []
A_list.append(A)
A_list.append(B)
A_list.append(C)
A_list = sorted(A_list)

if A_list[2] - A_list[1] == A_list[1] - A_list[0]:
    print('Yes')
else:
    print('No')