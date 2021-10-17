N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*xy)]

C = list(map(lambda a,b: a / b, A,B)) # 燃え尽きるまでにかかる秒数
doukasen_left = sum(C) / 2 # 両方から燃やせば半分の時間で燃え尽きるはず

ans = 0 # 左から何センチか
for i in range(N):
    doukasen_left -= C[i]
    if doukasen_left == 0:
        ans += A[i]
        break
    elif doukasen_left > 0:
        ans += A[i]
    elif doukasen_left < 0:
        ans += B[i] * (doukasen_left+C[i])
        break

print(ans)