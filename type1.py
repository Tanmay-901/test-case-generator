from random import randint

T = int(input("Enter value of T: "))
nmin = int(input("Enter min. value of n: "))
nmax = int(input("Enter max. value of n: "))
Amin = int(input("Enter min. value of Ai: "))
Amax = int(input("Enter max. value of Ai: "))
print(T)
for i in range(T):
    n = randint(nmin, nmax)
    a = [0] * n
    for j in range(n):
        a[j] = randint(nmin, nmax)
    print(n)
    print(*a)
