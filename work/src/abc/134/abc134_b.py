A, B = map(int, input().split())
look_range = (B*2)+1
if A % look_range != 0:
    ans = (A//look_range)+1
else:
    ans = A//look_range

print(ans)