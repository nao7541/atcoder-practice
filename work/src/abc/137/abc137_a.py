A, B = map(int, input().split())
a = A+B
b = A*B
c = A-B

print(max(a, max(b,c)))