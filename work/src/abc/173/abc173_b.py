N = int(input())
#空のリスト
A = []
#リストAにappend()を使って格納していく
for _ in range(N):
    A.append(input())

AC = 0
TLE = 0
WA = 0
RE = 0
for i in range(N):
    if A[i] == 'AC':
        AC += 1
    elif A[i] == 'TLE':
        TLE += 1
    elif A[i] == 'WA':
        WA += 1
    else:
        RE += 1
print('AC x '+ str(AC))
print('WA x '+ str(WA))
print('TLE x '+ str(TLE))
print('RE x '+ str(RE))