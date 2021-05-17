A, B, C= map(int, input().split())
if A > B:
    print('Takahashi')
elif A < B:
    print('Aoki')
else:
    print('Aoki' if C == 0 else 'Takahashi')