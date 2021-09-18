A, B = map(int, input().split())
dice_min = A
dice_max = 6 * A

if B < dice_min or dice_max < B:
    print('No')
else:
    print('Yes')