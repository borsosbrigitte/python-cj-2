# print("Curs 4")
# nr = input("Va rugam introduceti un nr")
# try:
#     nr = int(nr) * 2
#     print("Dublul numarului este: {}".format(nr))
# except:
#     print("A aparut o eroare!")
# else:
#     print("Totul e ok! {}")

# Functions


# def my_func():
#     print("My very first function!")
#
#     return
#
#
# result  = my_func()
# print("Result is {}".format(result))

#
# def A():
#     print("Ex 1")
#
#
# def B():
#     print("Ex 2")
#
# def C():
#     A()
#     B()
#
#
# C()

# def adunare(param1, param2):
#     """
#     prints the sum of the two params
#     :param param1:
#     :param param2:
#     :return: None
#     """
#     suma = param1 + param2
#     return suma
#
#
# primul_nr = input("Introdu primul nr: \n")
#
# al_doilea_nr = input("Introdu al doilea nr: \n")
#
# print(adunare(int(primul_nr), int(al_doilea_nr)))

#
# def ziNastere(prenume, nume="Moldovan", varsta=18):
#     print("Buna {} {}! La multi ani pentru cei {} ani!".format(nume, prenume, varsta))
#
#
# ziNastere(varsta=20, prenume="Ionut", nume="Popa")
# ziNastere(prenume="Cristian", varsta=30, nume="Popa")
# ziNastere("Maria")
#
# x = 2
#
#
# def Test():
#     x = 3
#     print(x)
#
# print(x)
# Test()
# print("Daca apelam functia Test(), vom avea rezultatul")
#
# def Suma(a, b, *c):
#     """
#     adunam cel putin 2 parametrii
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#
#     x = a + b
#     if c:
#         print("c = > {}".format(c))
#         for e in c:
#             x = x + e
#
#     return x
#
#
# print(Suma(1, 2))
# print(Suma(1, 2, 3, 4, 5))

# def F(b, **a):
#     print(a)
#     print(b)
#
#
# F("Parametrul b", unu=1, doi=2)
#
# Adunare  = lambda a, b: a + b
# print(Adunare(1,2))
#
# Cub = lambda  x: x**3
#
# print(Cub(2))

# prima problema

# def inlocuire(string):
#
#     if isinstance(string, str):
#         string = string.replace(" ", "_")
#         string = string.replace("e", "i")
#         string =string.replace("E", "I")
#
#         return string
#     else:
#         print("Dati va rog un sir de caractere")
#
# print(inlocuire("Merele, perele si pestele nu au E-uri"))

# a2a problema

def aparitii(string):
    d = dict()
    for n in string:
        keys = d.keys()
        if n in keys:
            d[n] = d[n] + 1
        else:
            d[n] = 1
    return d


print(aparitii("hello"))