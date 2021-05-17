N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_max = max(A)
b_min = min(B)
if b_min < a_max:
    print(0)
else:
    print(b_min - a_max + 1)