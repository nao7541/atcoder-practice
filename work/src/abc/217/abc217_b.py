S = []
for _ in range(3):
    S.append(input())

S_list = ['ABC', 'ARC', 'AGC', 'AHC']

for i in S_list:
    if i not in S:
        print(i)
        exit()