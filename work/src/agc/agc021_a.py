A = [s for s in input()]

A0 = A[0]
ans = 0
if len(A) == 1:
    print(int(A0))
    exit()
elif A0 == '1':
    if all(item == '9' for item in A[1:]):
        A0_int = int(A0)
        nines = 9 * (len(A) - 1)
        print(A0_int + nines)
        exit()
    else:
        print(9*(len(A)-1))
        exit()
elif all(item == A0 for item in A):
    print(9*len(A))
    exit()
else:
    if all(item == '9' for item in A[1:]):
        A0_int = int(A0)
        nines = 9 * (len(A) - 1)
        print(A0_int + nines)
        exit()
    else:
        A0_int = int(A0)
        nines = 9 * (len(A) - 1)
        print(A0_int + nines-1)
    """ A0_int = int(A0)
    nines = 9 * (len(A) - 1)
    print(A0_int + nines-1)
    exit() """