A, B= map(int, input().split())

if A < 10:
    B += 100*(10-A)
print(B)