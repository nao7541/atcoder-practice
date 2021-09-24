N = int(input())
mountains = []
for i in range(N):
    a,b=input().split()
    mountains.append([a, int(b)])
name, height = [list(i) for i in zip(*mountains)]

h_sort = sorted(height)
no2_index = height.index(h_sort[-2])
print(name[no2_index]) 
