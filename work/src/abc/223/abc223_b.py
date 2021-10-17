S = input()

max_s = S
min_s = S

for i in range(len(S)):
    tmp = S[0]
    S = S[1:] + tmp
    if S < min_s:
        min_s = S
    if max_s < S:
        max_s = S

print(min_s)
print(max_s)