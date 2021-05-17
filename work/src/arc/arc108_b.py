N = int(input())
s = input()

while 'fox' in s:
    s = s.replace('fox', '')

print(len(s))