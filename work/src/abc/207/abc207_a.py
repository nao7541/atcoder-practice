A, B, C = map(int, input().split())

ab = A+B
ac = A+C
bc = B+C
print(max(ab, max(ac, bc)))