import math
A, B, H, M = map(int, input().split())

minute = M*6
hour = H*30+M*0.5
if abs(minute-hour) <= 180:
    angle = abs(minute-hour)
else:
    d = 360 - max(minute, hour)
    angle = d+min(minute, hour)
cos = math.cos(math.radians(angle))

ans = math.sqrt(A**2 + B**2 - 2*A*B*cos)

print(ans)