N = int(input())
W = list(map(int,input().split()))
minimum = 100000000000000000000000000
for i in range(1, N):
    W_1 = sum(W[:i])
    W_2 = sum(W[i:])
    W_div = abs(W_1 - W_2)
    if W_div < minimum:
        minimum = W_div
        

print(minimum)