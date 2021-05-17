N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def probrem(A, B):
    AB_div = [x - y for (x, y) in zip(A, B)]
    count_less_than_0 = sum(x<0 for x in AB_div)
    sum_less_than_0 = sum([i for i in AB_div if i < 0])
    less_than_0 = [i for i in AB_div if i < 0]
    more_than_0 = [i for i in AB_div if i > 0]
    more_than_0.sort(reverse=True)
    ans = 0
    if sum(A) < sum(B):
        return -1
    if count_less_than_0 == 0:
        return 0
    for i in more_than_0:
        ans += 1
        sum_less_than_0 += i
        if sum_less_than_0 >= 0:
            break
    
    return ans + count_less_than_0

print(probrem(A, B))