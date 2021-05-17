import math

a = int(input())
# 入力された値の平方根まで計算できれば良い
# math.floorで小数点以下を切り捨て
m = math.floor(math.sqrt(a)) + 1
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, m):
        if n % i == 0:
            return False
    return True

sub = is_prime(a)
print(sub)