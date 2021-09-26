memo = {1:1, 2:1} # 辞書に終了条件の値を入れる

def fibonacci(n):
    if n in memo:
        return memo[n] # 辞書に登録されていれば、その値を返す
    
    memo[n] = fibonacci(n-2) + fibonacci(n-1) # 辞書に登録がなければ計算して辞書に登録する
    return memo[n]