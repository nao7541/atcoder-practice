value = [500, 100, 50, 10, 5, 1]
X = int(input())

result = 0
for i in range(6):
    add = X // value[i]
    X -= add * value[i]
    result += add

print(result)