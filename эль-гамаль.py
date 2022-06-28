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


p = int (input("p = "))
g = primitive_root(p)
print("Первообразный корень: ",g)
#Отправитель
x = int (input("x = "))
if 1 < x < p - 1:
    print("Соответствуют условии!!")
else :
    print("Заданное число не соответствуют условию!")

y = (g ** x) % p  #<<<<Ашык килт
print("<<<<<<<<<<<<<Открытый ключ>>>>>>>>>>>>>\n","y=", y, "g=", g, "p=", p,)
print("<<<<<<<<<<<<<Закрытый ключ>>>>>>>>>>>>>\n",x)


m = int(input("m = "))
if m < p:
    print("Соответствуют условии!")
else:
    print("Заданное число не соответствуют условию!")

k = int(input("Введите сессионный ключ k = "))
if 1 < k < p-1:
    print("Соответствуют условии!")
else:
    print("Заданное число не соответствуют условию!")


a = (g ** k) % p
b = m * (y ** k) % p
print("Шифротекст: ", "(",a, ",", b,")")
#Получатель
m_ = b * (a ** (p - 1 - x)) % p  # Дешифровать
print("Сообщение: ", m_)
if m == m_:
    print("Данные соответствуют!")
else:
    print("Данные не соответствуют")
