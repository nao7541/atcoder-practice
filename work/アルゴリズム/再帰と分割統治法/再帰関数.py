"""
１からNまでの総和を計算する再帰関数
"""
N = int(input())
def func(i):
    # N=0の場合は再帰呼び出しを行わず、直接０を返す
    # このベースケースの処理を怠ると再帰呼び出しを無限に繰り返すことになる
    if i == 0:
        return 0
    # 再帰的に答えを求めて出力する
    result = i + func(i-1)
    print(str(i)+"までの和"+str(result))

    return result

func(N)