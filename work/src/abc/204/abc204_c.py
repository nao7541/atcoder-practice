# おまじない
# このおまじないは再帰を行う上限をあげている(デフォルトは1000で、これだとエラーを起こす)
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

# Gは都市iから直接繋がっている都市のリスト
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)

# DFS(深さ優先探索)
def dfs(v):
    if temp[v]:
        # 同じ頂点を２度調べないため
        return
    temp[v] = True
    for vv in G[v]:
        dfs(vv)

ans = 0

# 都市の数だけループを回す
for i in range(N):
    temp = [False]*N
    # ここでtemp[j]は都市jに到達することが可能かどうかを示している
    dfs(i)
    ans += sum(temp)

print(ans)
