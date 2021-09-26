import itertools

S, K = map(str, input().split())

all = itertools.permutations(S, len(S))
comb_list = []

for x in all:
    comb_list.append(''.join(x))
    
    
comb_list = list(set(comb_list))
comb_list = sorted(comb_list)
print(comb_list[int(K)-1])