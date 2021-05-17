import collections

a = int(input())
a_str = [input() for i in range(a)]
b = int(input())
b_str = [input() for i in range(b)]

c = dict(collections.Counter(a_str) - collections.Counter(b_str))

if not bool(c):
    print(0)
else:
    print(max(c.values()))

# print(c)

#if max(c.values()) >= 0:
#    print(max(c.values()))
#else:
#    print(0)
