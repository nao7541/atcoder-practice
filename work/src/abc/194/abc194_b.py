N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*xy)]

a_min = min(A)
a_min_index = A.index(min(A))
b_min = min(B)
b_min_index = B.index(min(B))
if a_min_index != b_min_index:
    print(max(a_min, b_min))
else:
    a_min_second = sorted(A)[1]
    b_min_second = sorted(B)[1]
    sum_time = a_min + b_min
    if sum_time <= b_min_second and sum_time <= a_min_second:
        print(sum_time)
    else:
        if a_min == a_min_second or b_min == b_min_second:
            print(max(b_min_second, a_min_second))
        else:
            print(min(b_min_second, a_min_second))
        
    