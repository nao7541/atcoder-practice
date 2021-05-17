X, Y = map(int, input().split())

ans = "No"

for i in range(X+1):
    a = 2*i
    b = Y - a
    if b - 4*(X-i) == 0:
        ans = "Yes"
        break

print(ans)
