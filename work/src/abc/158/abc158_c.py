A,B = map(int,input().split())

a_num = A / 0.08
b_num = B / 0.1

tax_list = list(range(1, 101))



if a_num > b_num:
    if b_num + 10 > a_num:
        print(int(a_num))
    else:
        print(-1)
elif a_num == b_num:
    print(int(a_num))
else:
    if a_num + 12.5 > b_num:
        print(int(b_num))
    else:
        print(-1)

#print(b_num)