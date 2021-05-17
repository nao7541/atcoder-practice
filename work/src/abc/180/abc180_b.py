import math
a = int(input())
num = list(map(int,input().split()))

man = abs(num)
man = sum(man)

y = 0
for i in range(a):
    y += num[i] ** 2
y = math.sqrt(y)

t = abs(num)
t = max(t)

print(man)
print(y)
print(t)