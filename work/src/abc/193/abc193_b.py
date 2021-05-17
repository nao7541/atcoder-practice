import numpy as np
N = int(input().strip())

grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)

lowest_price = 1000000000000

grid = np.array(grid)

for n in range(N):
    take_minutes = grid[n][0]
    grid[n][2] -= take_minutes
    if grid[n][2] >= 1:
        if grid[n][1] < lowest_price:
            lowest_price = grid[n][1]
            
if lowest_price == 1000000000000:
    lowest_price = -1

print(lowest_price)