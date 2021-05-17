N,Q = map(int,input().split())
o = [list(map(int, input().split())) for l in range(Q)]
par = [i for i in range(N+1)]


def find(x):
    '''
    自分が親である時は自分の番号を返し、それ以外の時はもう一度findを行うと同時に、
    つなぎなおす(経路圧縮)
    '''
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) # 経路圧縮
        return par[x]

def same(x, y):
    """ 
    お互いの親が一緒であるか動かを判断する
    """
    return find(x) == find(y)

def unite(x, y):
    '''
    それぞれの親を確認して異なる場合のみ親を統一する
    '''
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

ans = 0
for i in range(Q):
    par = [i for i in range(N+1)] # 毎回木を作成する
    for j in range(Q):
        if i != j: # i番目の木はスキップする
            unite(o[j][0], o[j][1])
    
    flg = 0
    for j in range(1, N+1): # 各頂点について見ていく
        for k in range(j, N+1): # 頂点(j, k)がつながっているか(重複させないためにjから始める)
            if not same(j, k): # もし親が違う場合はつながっていないことがわかる。
                flg = 1
    
    if flg == 1: # フラグが立っているときはその辺は橋だとわかるため、１増やす
        ans += 1

print(ans)