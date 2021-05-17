"""
フィボナッチ数列の第Ｎ項を求める再帰関数
→再帰関数内で再帰呼び出しを複数回行う
"""

# def fibo(N):
#    if N == 0:
#        return 0
#    elif N == 1:
#        return 1
#    
#    return fibo(N-1) + fibo(N-2)

"""
ただ、これだと同じ計算を何度も実行していて効率が非常に悪い
"""
# for文の反復で求める
F = [0,1]
for N in range(2,50):
    F.append(F[N-1] + F[N-2])
    # print(str(N)+"項目："+str(F[N]))
# これにより、計算量はN-1で済むようになる

"""
じゃあ再帰関数で同じようにすることはできないの？
→同じ引数に対する答えをメモ化することで可能になる(いわゆるキャッシュという考え方)
"""
# フィボナッチ数列を求める再帰関数をメモ化
memo = [-1] * 50

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # メモをチェック(すでに計算済みなら答えをリターンする)
    if memo[N] != -1:
        return memo[N]

    # 答えをメモ化しながら、再帰呼び出し
    memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

fibo(49)
for N in range(2, 50):
    print(str(N)+"項目："+str(F[N]))
# このメモを行うことで計算量をO(N)にすることができる