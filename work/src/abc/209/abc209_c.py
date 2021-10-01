import sys
input = sys.stdin.readline
N = int(input())
C = list(map(int, input().split()))
ans = 1
C = sorted(C)

for i in range(N):
    comb = C[i] - i
    if comb <= 0:
        ans *= 0
        break
    else:
        ans *= comb
        # 数値を10**9+7で割った余りを出力する必要がある問題については最後に割るのではなく、毎回割ってあげないと実行時間が肥大化してしまう
        ans %= 10**9+7


print(ans)