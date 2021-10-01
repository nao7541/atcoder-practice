N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

jewel = [10000000000] * N
jewel[0] = T[0]

for i in range(1,N):
    t = T[i]
    s = jewel[i-1] + S[i-1]
    jewel[i] = min(t, s)

t = jewel[0]
s = jewel[N-1] + S[N-1]
jewel[0] = min(t, s)

for i in range(1,N):
    t = T[i]
    s = jewel[i-1] + S[i-1]
    jewel[i] = min(t, s)

for i in jewel:
    print(i)
    
# 上のやり方でもACすることができるが、同じforループを2回書いているため、下の余りを用いた方法だと1回のforループで済む
""" for i in range(N*2):
    jewel[(i+1)%N] = min(T[(i+1)%N], jewel[i%N] + S[i%N]) """