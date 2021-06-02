N = int(input())
digit = len(str(N))
ans = 0
comma = digit // 3
# 3の倍数の桁に関してはカンマは増えないので1引く
if digit % 3 == 0:
    comma -= 1

# カンマが２個以上付くときの処理
for i in range(1, comma):
    a = 1000**i
    b = 1000**(i+1)
    ans += (b-a)*i

# 一番上のカンマのカウント
a = 1000**comma
ans += (N-a+1)*comma
print(ans)
