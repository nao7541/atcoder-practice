import math

N = int(input())
# 入力された値の平方根まで計算できれば良い
# math.floorで小数点以下を切り捨て
m = math.floor(math.sqrt(N)) + 1
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, m):
        if N % i == 0:
            return False
    return True

if is_prime(m) == True:
    print(N-1)
    exit()

tmp = 100000000000000000
for i in range(2, m):
    if N % i == 0:
        a = i + (N//i)
        if a < tmp:
            tmp = a

print(tmp-2)