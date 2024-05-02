# Používáme u dat, které víme, že v budoucnu nebudeme měnít
coordinates = (3, 5)
print(coordinates)
print(coordinates[1])     # vypise 5

#  Vypiš ('cherry', 'orange', 'kiwi') z tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Vypis ('apple', 'banana', 'cherry', 'orange')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[0:4])

# Nahrad hodnotu banana hodnotou coconut v tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "coconut"
x = tuple(y)
print(x)

# Pridej hodnotu "car" do tuples:

thistuple1 = ("apple", "banana", "cherry")
x = list(thistuple1)
x.append("car")
thistuple1 = tuple(x)
print(thistuple1)

# Přidej tuple = ("orange,) do tuple
thistuple2 = ("apple", "banana", "cherry")
y = ("orange",)
x = thistuple2 + y
print(x)


# Odstranění hodnoty apple z tuple.
thistuple3 = ("apple", "banana", "cherry")
x = list(thistuple3)
x.remove("apple")
y = list(x)
print(y)


# Odstran tuple
thistuple4 = ("apple", "banana", "cherry")
del thistuple4

# Extrahuj hodnoty v tuples do promennych:
fruits = ("apple", "banana", "cherry")
(black, red, green) = fruits
print(black)
print(red)
print(green)


# Pouzití hvezdicky u poslední proměnné. Když chceme použít méně proměnných než je hodnot v tuples.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(black, red, *green) = fruits
print(black)
print(red)
print(green)

# Pouzití hvezdicky u vnitrni proměnné.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(black, red, *green, yellow) = fruits
print(black)
print(red)
print(green)
print(yellow)

# Vypise vsechny hodnoty pomoci for metody:
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

# Vypise vsechny hodnoty v tuple dle jejich indexu
thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
    print(thistuple1[i])

# Pouzij while loop pro vypis hodnot
thistuple2 = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple2):
    print(thistuple2[i])
    i = i + 1



# Scitani tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

# Nasobeni tuple krát 2:
fruits = ("apple", "banana", "cherry")


# Vypis kolikrat se vyskytuje cislo 3 v tuples
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(3))

# Na kterem miste se vyskytuje cislo 4
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

