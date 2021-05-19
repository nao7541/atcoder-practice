A, B, C= map(int, input().split())

n = A // (B+C)
amari = A % (B+C)
ans_1 = n * B
if amari >= B:
    ans_2 = B
else:
    ans_2 = amari
print(ans_1+ans_2)