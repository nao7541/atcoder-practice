N, K= map(int, input().split())

a = N % K # 負の数に行った時の絶対値
b = abs(a-K)

print(min(a,b))