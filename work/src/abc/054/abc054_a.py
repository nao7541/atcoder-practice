A,B = map(int,input().split())
def poker(A, B):
    ans = ''
    if A > B:
        ans = 'Alice'
    elif A < B:
        ans = 'Bob'
    else:
        ans = 'Draw'
    if A == 1:
        if A == B:
            ans = 'Draw'
        else:
            ans = 'Alice'
    elif B == 1:
        if A == B:
            ans = 'Draw'
        else:
            ans = 'Bob'
    return ans

print(poker(A, B))