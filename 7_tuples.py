# Používáme u dat, které víme, že v budoucnu nebudeme měnít
coordinates = (3, 5)
print(coordinates)
print(coordinates[1])     # vypise 5

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])   # ('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])    # ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])   # ('orange', 'kiwi', 'melon')

# If pouzit v tuples
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# V tuples nemuzeme menit hodnoty, proto nejdriv musime konvertovat do listu, zmenit hodnotu a pak konvertovat na tuples
x = ("apple", "banana", "cherry")
y = list(x)     # konvertovani tuple na list
y[1] = "kiwi"   # nahrazeni druhe hodnoty za kiwi
x = tuple(y)    # konvertovani listu zpet na tuple

print(x)


# V tuples nemuzeme pridavat hodnoty, proto nejdriv musime konvertovat do listu, pridat hodnotu a pak konvertovat na tuples

thistuple1 = ("apple", "banana", "cherry")
y = list(thistuple1)
y.append("car")
thistuple1 = tuple(y)

print(thistuple1)

# Můžeme přidávat tuple do tuple
thistuple2 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple2 += y
print(thistuple2)

# Odstranění hodnoty z tuple. Opět musíme převézt na list
thistuple3 = ("apple", "banana", "cherry")
y = list(thistuple3)
y.remove("banana")
thistuple3 = tuple(y)

print(thistuple3)


# úplné odstranění tuple
thistuple4 = ("apple", "banana", "cherry")
del thistuple4


# Můzeme extrahovat hodnoty v tuples do promennych:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Pouzití hvezdicky u poslední proměnné. Když chcem použít méně proměnných než je hodnot v tuples.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)    # proměnná red vypíše zbylé hodnoty jako seznam


# Pouzití hvezdicky u vnitrni proměnné.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
