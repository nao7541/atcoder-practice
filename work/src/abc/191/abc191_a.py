V, T, S, D= map(int, input().split())
hide_start = V * T
hide_end = V * S

is_hit = hide_start <= D and D <= hide_end
if is_hit:
    print('No')
else:
    print('Yes')