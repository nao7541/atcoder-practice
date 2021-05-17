from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()
ans = 0
for b in B:
    t = bisect_left(A, b)
    s = bisect_right(C, b)
    ans += t*(len(C)-s)

print(ans)