a, b = map(int, input().split())
c = input()

for i in c:
    if i == "o":
        b += 1
    if i == 'x':
        if b == 0:
            continue
        else:
            b -= 1

print(b)