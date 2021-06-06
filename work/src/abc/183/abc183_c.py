from itertools import permutations

N,K = map(int,input().split())
T = []
for _ in range(N):
    s = list(map(int, input().split()))
    T.append(s)

ans = 0

for per in permutations(range(1, N)):
    score = 0 # この訪問順でかかった時間
    prev = 0 # 初めは都市0からスタートする
    for i in range(N-1):
        cur = per[i]
        score += T[prev][cur] # 都市prevからcurに向かう
        prev = cur
    score += T[prev][0] # 最後に都市0に帰ってくる
    
    if score == K:
        ans += 1

print(ans)