import string
X = input()
N = int(input())
S = []
#リストAにappend()を使って格納していく
for _ in range(N):
    S.append(input())

str_list1 = [x for x in X]
# string.ascii_loqercaseは'abcdefghijklmnopqrstuvwxyz'を返す
str_list2 = list(string.ascii_lowercase)
str_dic = dict(zip(str_list1, str_list2))

# 新しい辞書順を元の辞書順でソートできるように文字を置き換える関数
def change_string(befo_str):
    af_str = ''
    for i in befo_str:
        af_str += str_dic[i]
    return af_str

# keyに関数を入れることにより、関数を適用した上でソートを実行してくれる
S.sort(key=change_string)
for s in S:
    print(s)