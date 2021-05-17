N = list(map(int, input().split()))
input_line = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
ans = []
for i in range(len(input_line)):
    num = alp.find(input_line[i])
    num = int(num)
    if N[num] > 0:
        ans.append(input_line[i])
        N[num] -= 1
    else:
        continue
    num = 0

print(''.join(ans))