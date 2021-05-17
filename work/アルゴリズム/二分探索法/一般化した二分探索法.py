a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]

# xが条件を満たすかどうか
def isOk(x, key):
    if a[x] >= key:
        return True
    else:
        return False

# P(x) = true となる差k賞の整数xを返す
def binary_search(key):
    left = -1 # x=0が条件を満たす可能性もあるため、-1にしておく
    right = len(a) # 「x = len(x)-1」が条件を満たさない可能性もあるから、len(x)にする

    while right - left > 1:
        mid = left + (right - left) // 2

        if isOk(mid, key):
            right = mid
        else:
            left = mid

    return right

print(binary_search(51))

