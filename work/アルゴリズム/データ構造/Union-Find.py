'''
N: 頂点の個数
Q: クエリの個数
par: 各頂点に対応する親を入れる。最初は各要素自身が親となる
i番目のクエリの種類を表す整数とクエリの対象となる頂点の番号を表す整数を入れる
'''
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
