import os
import statistics

def quickSort(a):
    # 配列のメジアンよりも小さい要素を集めた配列
    left = []

    # 配列のメジアンよりも大きい要素を集めた配列
    right = []

    # 再帰の停止条件
    # 再帰的に配列を分割した後の、要素数が１以下になったら停止する
    if len(a) <= 1:
        return a
    
    # 配列の中央値を取得する
    median = int(statistics.median(a))

    # 配列内に含まれる中央値の個数を数えるための変数
    medianFlg = 0

    for i in a:
        # 配列の要素が中央値より小さければleftに格納
        if i < median:
            left.append(i)
        
        # 配列の要素が中央値より大きければrightに格納
        elif i > median:
            right.append(i)
        
        else:
            # 要素が中央値の場合は、フラグに１を加える
            medianFlg += 1
    
    print(left)
    print(right)

    # 配列left, rightごとに再帰を行い、配列を小さくしていく
    left = quickSort(left)
    right = quickSort(right)

    # 配列left、中央値のmedian、配列rightを結合したものを返す
    return left + [median] * medianFlg + right

a = [10, 12, 15, 3, 8, 17, 4, 1]
print(quickSort(a))

# 平均時間計算量はO(N * logN)
# 最悪時間計算量はO(N**2)
# 実用上はマージソートよりも高速に動作すると言われている