"""
N個の整数a0,a1...と正の整数Wが与えられる。a0,a1...の中から何個かの整数を選んで総和をWと
することができるかどうか判定する
"""
N, W = map(int, input().split())
# a = list(map(int, input().split()))

# bitは2**N通りの部分集合全体を動く
#exist = False
#for bit in range(2**N):
#    total = 0 # 部分集合に含まれる要素の和
#    for i in range(N):
        # i番目の要素a[i]が部分集合に含まれているかどうか
#        if bit & (1 << i):
#            total += a[i]

    # totalがWに一致するかどうか
#    if total == W:
#        exist = True

#print(exist)

# このアルゴリズムは2**N通りの場合についてiが0,1...N-1を動くため、計算量はO(N*2**N)となり、効率的とは言えない
# しかし、動的計画法を用いると劇的に早くなる
"""
問題を読み替えて、a0,a1...のうち、最初のi個から何個か選んで、総和をwにできるかどうかをブール値で返す
"""
# 部分和問題を再帰関数を用いる全探索で解く
a = []
for i in range(N):
    a.append(i)

def func(i, w, a):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        return True
    
    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        return True
    
    # どちらもfalseの場合はfalse
    return False

# 再帰的に解く
if func(N, W, a):
    print("Yes")
else:
    print("No")
# このアルゴリズムの計算量はO(2**N)となり、最初のものよりも減っていることがわかる