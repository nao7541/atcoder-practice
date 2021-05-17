print('Start Game!')

# 対象の数の候補を表す区間を[left, right)で表す
left = 20
right = 36

# 数を一つに絞れないうちは繰り返す
while right - left > 1:
    mid = left + (right - left) // 2

    # mid以上か聞いて、解答をyes/noで受け取る
    print("Is the age less than"+ str(mid) + "?(yes / no)")

    ans = input()
    if ans == "yes":
        right = mid
    else:
        left = mid

# 当てる
print("The age is"+str(left)+"!")