A, B, C = map(int, input().split())

if abs(A) == abs(B):
    if A == B:
        print('=')
        exit()
    elif A > B:
        if C % 2 == 0:
            print('=')
            exit()
        else:
            print('>')
            exit()
    elif A < B:
        if C % 2 == 0:
            print('=')
            exit()
        else:
            print('<')
            exit()

if A >= 0 and B >= 0:
    if A > B:
        print('>')
    else:
        print('<')

elif A >= 0 and B < 0:
    if C % 2 != 0:
        print('>')
    else:
        if A > abs(B):
            print('>')
        else:
            print('<')

elif A < 0 and B >= 0:
    if C % 2 != 0:
        print('<')
    else:
        if abs(A) > B:
            print('>')
        else:
            print('<')

elif A < 0 and B < 0:
    if C % 2 != 0:
        if A < B:
            print('<')
        else:
            print('>')
            