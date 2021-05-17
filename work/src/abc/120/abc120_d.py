N,Q = map(int,input().split())
o = [list(map(int, input().split())) for l in range(Q)]

par = [i for i in range(N+1)]

#ランク(深さ）
rank = [0]*(N+1)

size = [1]*(N+1) # 各要素が属するグループのサイズ
import sys
sys.setrecursionlimit(100000)



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

    ####ランクあり
    if rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]
        if rank[x] == rank[y]:
            rank[y] += 1

ans = [0] * Q

ans[Q-1] = N*(N-1)//2 # すべての橋が壊れているときの不便度

# 橋の情報を逆順に取り出す
for i in range(Q-1, 0, -1):
    a = o[i][0]
    b = o[i][1]
    if find(a) != find(b):
        # 親が同じではないとき、aとbをつないだら同じになるから、
        # aとbのグループの要素の組み合わせの数だけ不便度が減る
        ans[i-1] = ans[i] - size[find(a)] * size[find(b)]
    else:
        # 親が同じときはつないでも不便度は変わらない
        ans[i-1] = ans[i]

    # 橋を繋げる
    unite(a,b)

for a in ans:
    print(a)