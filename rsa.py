import math


def nod(a, b):
    if (a == 0):
        return b
    return nod(b % a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if (nod(i, n) == 1):
            result += 1
    return result

def IsPrime_solo(y):
    t = 2
    while y % t != 0:
        t += 1
    return t == y

def IsPrime(a1, b1):
    while b1 * b1 <= a1 and a1 % b1 != 0:
        b1 += 1
    return b1 * b1 > a1


p = int(input("p = "))
q = int(input("q = "))
if IsPrime_solo(p):
    if IsPrime_solo(q):
        N = p * q
        print("N = ", N)
    else:
        print("Число q не простое!")
else:
    print("Число p не простое!")

Euler = phi(N)
print("Эйлер N: ",Euler)
e = int(input("e = "))
if e > 1 and Euler > e:
    if (IsPrime(e, Euler)) == True:
        m = int(input("m = "))
        c = (math.pow(m,e)) % N
        print("c = ", int(c))
        l = phi(Euler) - 1
        d = (math.pow(e, l)) % Euler
        print("d = ", int(d))

    else:
        print("Ошибка")
else:
    print("Ошибка")





