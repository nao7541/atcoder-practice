from itertools import combinations
N = input()
now = 0
for i in range(len(N)):
    now += int(N[i])
# そもそも合計が３の倍数ならここで終わる
if now % 3 == 0:
    print(0)
    exit()

# 何桁消すかを決めるためのi
for i in range(1, len(N)):
    # 組み合わせを算出するためのcomb
    for comb in combinations(range(len(N)), i):
        div = 0
        # 消す文字を決めるためのj
        for j in comb:
            div += int(N[j])
        if (now-div) % 3 == 0:
            print(i)
            exit()

print(-1)