N = int(input())

a = 1000 * (N//500)
N -= 500*(N//500)
b = 5 * (N//5)
print(a+b)