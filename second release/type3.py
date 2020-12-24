from random import randint
T = int(input("Enter value of T: "))
Amin = int(input("Enter min. value of Ai: "))
Amax = int(input("Enter max. value of Ai: "))
Bmin = int(input("Enter min. value of Bi: "))
Bmax = int(input("Enter max. value of Bi: "))
print(T)
for i in range(T):
    a = randint(Amin, Amax)
    b = randint(Bmin, Bmax)
    print(a,b)
