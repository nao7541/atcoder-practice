def MergeSort(a):
    n = len(a)

    if len(a) == 1:
        return a
    
    # 整列されていないリストを２つのサブリストに分割する
    # 真ん中をmidとする
    mid = int(round(n/2))

    left = a[:mid]
    right = a[mid:]

    print(left, right)

    # 分解したリストを整列する。サブリストもマージソートを使って整列させる
    l = MergeSort(left)
    r = MergeSort(right)

    # 2つのサブリストをマージして１つの整列済みリストにする
    return Merge(l, r)



# 整列済みリストx,yを使って、整列済みリストzを作成する
def Merge(x, y):
    z = []

    # xとyの先頭のどちらかの数字を比較し、小さいほうをzに追加し、その値を削除
    # この手順をどちらかのリストが空になるまで続ける
    while (len(x) > 0) and (len(y) > 0):
        if x[0] < y[0]:
            z.append(x[0])
            del x[0]
        else:
            z.append(y[0])
            del y[0]
    
    # 残ったリストの要素をzの末尾に追加する
    if len(x) > 0:
        # リストで渡すからappendではなくextend
        z.extend(x)
    else:
        z.extend(y)

    return z

# 計算量はO(N * logN)

a = [12, 9, 15, 3, 8, 17, 6, 1]
print(MergeSort(a))