print("Curs 3")

# x = 10
# while x > 1:
#     print("x este {}".format(x))
#     x = x - 1

for i in range(1,10,2):
    print("i este {}".format(i))

for s in "some_string":
    print(s)

exemplu = "Acesta este un string"
print("prima litera din sir: {}".format(exemplu[0]))

print("ultima litera din sir este: {}".format(exemplu[-1]))
print("slicing de siruri de caractere")
print(exemplu[15:])
print(exemplu[-6:])

l = len(exemplu)
print("lungimea sirului este de {}".format(l))

# print(exemplu[0])
# exemplu[0] = 'B'
# print(exemplu[0])
exemplu = "noua valoare"
print(exemplu)

exemplu2 = exemplu.replace('a', 'b')
print(exemplu)
print(exemplu2)

x = "abcdef"
SEARCH_KEY = "a"
print("Litera cautata este r. Ea exista? {}".format(
    x.find(SEARCH_KEY))
)

y = "100,123,2,5"
l = y.split(",")

print(l)

something = None
A = (1, 2, 1)
B = (1, 2, 1)
C = (2, 4, 7)
D = A + B

print(D)
print(A)
print(B)
print(C)

print(A == B)
print(A == C)

# A[1] = 8
# print(A[1])

inventar  = ("faina", "drojdie", "apa", "sare")
print(inventar)

for item, value in enumerate(inventar):
    print("Produs {} => {}".format(item, value))

x = []
print(x)

if not x:
    print("Lista vida")
else:
    print("Lista are valori")

x = [True,
     False,
     "Ana",
     "are",
     "mere",
     2,
     3,
     ["un sir de caractere"],
     ("tuplu",2)
]

print(x)
x[2] = "Ion"
print(x[2])
print(x)

inventar = ["faina", "drojdie", "apa", "sare"]
for item, value in enumerate(inventar):
    print("Produs {} => {}".format(item, value))

for element in inventar:
    print(element)

inventar.append("coca-cola")
print(inventar)
inventar += ["pepsi"]
print(inventar)

produse_noi = ["mere", "pere", "mere", "portocale"]

# inventar = inventar + produse_noi
print(inventar)
inventar.extend(produse_noi)
print(inventar)
# inventar.sort()
print(inventar)
print(sorted(inventar))
print(inventar)

inventar.reverse()
print(inventar)

# print(inventar.count("mere"))
print(inventar.index("mere"))
print(inventar.index("pere"))

inventar.insert(1, "avocado")
print(inventar)

l = inventar[:2] + ["banane"] + inventar[2:]
print(l)

print(l[3:])

lista = [
    0,
    1,
    [
        "al doilea nivel",
        ["al treilea nivel", "abc"]
    ]
]

print(lista[2][0])
print(lista[2][1][1])

sir_nou = "acesta este un sir de caractere"
print(sir_nou[::])
print(lista[::2])

# Seturi

s1 = set({1, 2, 3, 4})
s2 = {3, 4, 5, 6}

print(s1)
print(s2)

s1.add(9)
s1.add(9)
print(s1)

# l = [1, 2, 3, 4, 5, 5, 6, 6, 9]
# print(l)
# s3 = set(l)
# l2 = list(s3)
# print(s3)
# print(l2)

s1 = set({1, 2, 3, 4})
s2 = set({3, 4, 5, 6})

print(s1 & s2) # intersectie
print(s1 | s2) # uniune
print(s1 - s2) # diferenta
print(s2 - s1) # diferenta
print(s1 ^ s2) # diferenta simetrica

print((s1 - s2) | (s2 - s1))

s2.add(9)
print(s2)
s2.discard(3)
print(s2)

# Dictionar

# d = dict()
d = {
     1: 'a',
     2: 'b'
}  # cheia trebuie sa fie unica

print(d[2])

d2 = {
    '1': "Salut"
}

print(d2)

# d3 = {
#     1: "Home"
#
# }
#
# print(d3[1])
#
# d3[1] = "Office"
#
# print(d3[1])

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}

print(my_dict)

print(my_dict.get(3, "Default"))
KEY = 3
if KEY in my_dict:
    print("True")
else:
    print("False")

print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())

for key, val in my_dict.items():
    print("{} => {}".format(key, val))

print(my_dict.pop(3))
print(my_dict)

del(my_dict[2])
print(my_dict)

