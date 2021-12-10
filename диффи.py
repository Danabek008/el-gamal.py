def nod(r, e):
    while r != e:
        if r > e:
            r = r - e
        else:
            e = e - r
    return r


def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo) if nod(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g


p = int(input("p = "))
g = primitive_root(p)
print("g = ",g)
a = int(input("Alisa a = "))
b = int(input("Bob b = "))

a_ = (g**a)%  p
print("A = ",a_)
b_ = (g**b) % p
print("B = ",b_)


k = (g ** (a*b)) % p
b__ = (b_ ** a) % p
print("k = ",k)
if b__ == k:
    print("<<<<<<<<<<<B>>>>>>>>>>>")
    print("B^a mod p = g^ab mod p")
    print("Условие соответствует!")
    print("Bob = ",b__)
else:
    print("<<<<<<<<<<<B>>>>>>>>>>>")
    print("B^a mod p = g^ab mod p")
    print("Условие не соответствует!")
    print("Bob = ",b__)

a__ = (a_ ** b) % p
if a__ == k:
    print("<<<<<<<<<<<A>>>>>>>>>>>")
    print("B^a mod p = g^ab mod p")
    print("Условие соответствует!")
    print("Alisa = ", a__)
else:
    print("<<<<<<<<<<<A>>>>>>>>>>>")
    print("B^a mod p = g^ab mod p")
    print("Условие не соответствует!")
    print("Alisa = ", a__)



