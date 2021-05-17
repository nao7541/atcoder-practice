a = int(input())
b = []

if a >= 8:
    a -= 8
    b.append(8)

if a >= 4:
    a-= 4
    b.append(4)

if a >= 2:
    a -= 2
    b.append(2)

if a >= 1:
    a -= 1
    b.append(1)

c = len(b)
print(c)
for i in range(c):
    print(b[i])
