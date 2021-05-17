import heapq
i = list(map(int, input().split()))
i = list(map(lambda x: x*(-1), i))
print(i)

heapq.heapify(i)
print(heapq.heappop(i)*(-1)) # 最大値の取り出し
print(i)