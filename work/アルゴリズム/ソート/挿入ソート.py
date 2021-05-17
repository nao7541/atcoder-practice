def insertion_sort(A):
    for j in range(1, len(A)): # 先頭はソート済みとする
        key = A[j] # ソートの対象をkeyとする
        i = j-1
        # keyと大きさを比較する対象であるj-1番目~先頭を変数iでループ
        while i >= 0 and A[i] > key:
            # A[i]がkeyよりも大きく、iが0以上ならA[i]を右にずらす
            A[i+1] = A[i]
            # 次の比較をするためにiを１減らす
            i = i - 1
        # A[i]がkeyよりも小さくなったら、A[i]の右に挿入するためにA[i+1]にkeyを代入
        A[i+1] = key
    return A

a = [4,1,3,5,2]
print(insertion_sort(a))


# 計算量はO(N**2)
# しかし、与えられた列がほとんど整数の時、高速に動く