count = 0 # 駒の置き方が何通りか格納する変数
board = [] # 盤上に置かれた駒を表すリスト


def deplication(x, y):
    """斜めの重複チェック"""
    for x1 in range(0, x):
        y1 = board[x1]
        if abs(x - x1) == abs(y - y1):
            return True
    return False


def n_queen(n, x):
    """
    xはクイーンを配置する行
    yはクイーンを配置する列
    1行ずつ配置していき最後の行まで配置できたらcountを+1する
    """
    global count
    if n == x:
        #print(board)
        count += 1
    else:
        for y in range(0, n):
            if y in board or deplication(x, y):
                continue
            board.append(y)
            n_queen(n, x + 1)
            board.pop()


n_queen(8, 0)
print(count)