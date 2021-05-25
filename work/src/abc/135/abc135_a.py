A, B = map(int, input().split())
if (A+B) % 2 != 0:
    print('IMPOSSIBLE')
else:
    ans = (A+B) // 2
    print(ans)