import sys
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_sort = sorted(a, reverse=True)
b_sort = sorted(b, reverse=True)
a_total = a[0] * a[1] * a[2]
b_total = b[0] * b[1] * b[2]

if b_sort[0] > a_sort[0]:
    print(0)
    sys.exit()

sub = a_total // b_total

print(sub)

