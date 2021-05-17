"""
区間分割とは、「１列に並んだN個の対象物を区間に分割する方法を最適化する問題」である
区間の表し方について、N個の要素が並んでいるとき、それらの要素の「両端」と「隙間」は合計でN+1個存在する。
それらに対して左から順に0,1,...Nと番号を振る。そこで区間の左端をl、右端をrとして、区間を[l,r)と表すこととする。

問：N個の要素が1列に並んでいて、これをいくつかの区間に分割したいものとする。各区間にはスコアc(l,r)がついているとする。
　　KをN以下の整数として、K+1個の整数t0,t1,...tkを0= t0<t1<...tk =Nを満たすように撮った時、区間分割のスコアを
　　Ct0t1 + Ct1t2 + ... Ctk-1tk
　　によって定義する。N要素の区間分割の仕方を全て考えたときの、考えられるスコアの最小値を求める
"""

inf = 200000000
N = int(input())

c = [[inf]*(N+1) for j in range(N+1)]

dp = [inf] * (N+1)
dp[0] = 0

for i in range(N+1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j]+ c[j][i])
