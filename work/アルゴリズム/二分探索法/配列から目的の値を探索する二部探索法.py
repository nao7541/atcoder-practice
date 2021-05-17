N = 8
a = [3,5,8,10,14,17,21,39]

# 目的の値keyの添え字を返す(存在しない場合は-1)
# 計算量はO(logN)となる
def binary_search(key):
    left = 0
    right = len(a)-1 # 配列aの左端と右端
    while right >= left:
        mid = left + (right - left) // 2 # 区間の真ん中
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid -1
        elif a[mid] < key:
            left = mid + 1
    
    return -1

print(binary_search(10))
print(binary_search(3))
print(binary_search(39))
print(binary_search(100))