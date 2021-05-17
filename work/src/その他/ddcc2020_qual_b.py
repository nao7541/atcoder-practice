num = int(input())
stick = list(map(int,input().split()))
half = (num // 2)
stick_a = stick[:half]
stick_b = stick[half+2:]

if num % 2 == 0:
    stick_a = stick[:half]
    stick_b = stick[half:]
else:
    stick_a = stick[:half]
    stick_b = stick[half+1:]
    if sum(stick_a) >= sum(stick_b):
        stick_b = stick_b.insert(0, stick[half])
    else:
        stick_a.append(stick[half])

while sum(stick_a) - sum(stick_b) > stick_a[-1] or :
    stick_b.append(stick_a[-1])
    stick_a.pop()
while sum(stick_b) - sum(stick_a) > stick_b[0]:
    stick_a.append(stick_b[0])
    stick_b.pop(0)

sub = abs(sum(stick_a) - sum(stick_b))

print(sub)
