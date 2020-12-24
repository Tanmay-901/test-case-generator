from random import randint
T = int(input("Enter value of T: "))
nmin = int(input("Enter min. value of n: "))
nmax = int(input("Enter max. value of n: "))
m_min = int(input("Enter min. value of m: "))
m_max = int(input("Enter max. value of m: "))
Amin = int(input("Enter min. value of Ai: "))
Amax = int(input("Enter max. value of Ai: "))
n = randint(nmin, nmax)
m = randint(m_min, m_max)
a = [0] * n
print(T)
for i in range(T):
    for j in range(n):
        a[j] = randint(nmin, nmax)
    print(n, m)
    print(*a)
