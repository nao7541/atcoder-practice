A, B, C = map(int, input().split())
if A >= C:
    A -= C
    print(A, B)
elif B >= (C-A):
    B -= (C-A)
    print(0, B)
else:
    print(0, 0)