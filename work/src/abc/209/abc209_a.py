A, B = map(int, input().split())

C = B-A+1
if C <= 0:
    print(0)
else:
    print(C)