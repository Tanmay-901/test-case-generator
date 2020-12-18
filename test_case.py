from random import randint
import os
print("select the type of test case you want want to generate from these types:")
print("1: T                    2: T                    3: T                    ")
print("   n                       m n                     A1 B1       ")
print("   A1 A2 A3 A4...          A1 A2 A3 A4...          A2 B2       ")
print("\nwhere T is the no. of test cases and other variables can be as per requirement")
print("Enter your choice:")
choice = int(input())
if choice == 1:
    T = int(input("Enter value of T: "))
    nmin = int(input("Enter min. value of n: "))
    nmax = int(input("Enter max. value of n: "))
    Amin = int(input("Enter min. value of Ai: "))
    Amax = int(input("Enter max. value of Ai: "))
    n = randint(nmin, nmax)
    a = [0]*n
    print(T)
    for i in range(T):
        for j in range(n):
            a[j] = randint(nmin, nmax)
        print(n)
        print(*a)
elif choice == 2:
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
elif choice == 3:
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
else:
    print("We are currently under development and will add other formats soon")
    y = input("do you wish to add some specific test case format, Y/N: ")
    if y == 'y' or y == 'Y':
        os.system('python new_format.py')
    else:
        print("Thank you")
