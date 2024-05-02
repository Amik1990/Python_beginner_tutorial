# Pouziti loop v tuple

# Vypise vsechny hodnoty v tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Vypise vsechny hodnoty v tuple dle jejich indexu
thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
    print(thistuple1[i])

# Pouziti while loop
thistuple2 = ("apple", "banana", "cherry")
i = 0     # zaciname nulou
while i < len(thistuple2):
    print(thistuple2[i])
    i = i + 1

# Scitani tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Nasobeni tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# metoda count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)     # vypise kolikrat se vyskytuje cislo 5 v tuple
print(x)

# metoda index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)      # vyhleda prvni vyskyt cisla 8 v tuple a vypise jeho index
print(x)
