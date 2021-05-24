A, B = map(int, input().split())
left = B - (A-1)
right = B + (A-1)
if left < -1000000:
    left = -1000000
if right > 1000000:
    right = 1000000
ans = []
for i in range(left, right+1):
    ans.append(str(i))

print(' '.join(ans))

