a = input()

a_list = list(a)

sub = 0

for i in range(len(a_list)):
    if a_list[i] == "2":
        sub += 1

print(sub)
