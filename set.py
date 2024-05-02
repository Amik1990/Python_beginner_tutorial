# neseřazené, můžeme měnit hondnoty, bez duplicit.
# Stejné značení jako slovníky, ale bez klíčů

myset = {1, 2, 3}  # kdbych dopsal další číslo 3, tak se nezobrazí.
print(myset)

# vytvoření prázdného setu:
myset = set()   # nemohu použít tohle:  myset = {} , protože python by si myslel, že chci vytvořít slovník!!!


# Příklad 1:
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)    # sloučí hodnoty odds a evens {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(u)

i = odds.intersection(primes)   #  vypíše shodné hodnoty z odds a primes {3, 5, 7}
print(i)


# Příklad2:  metoda difference vypíše hodnoty prvního setu, které se nevyskytují v druhém setu
#  symmetric_difference vypíše hodnoty, obou setů, které nejsou duplicitní navzájem mezi sety
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)   # {4, 5, 6, 7, 8, 9}
print(diff)
diff1 = setB.difference(setA)   # {10, 11, 12}
print(diff1)

diff3 = setB.symmetric_difference(setA)   # {4, 5, 6, 7, 8, 9, 10, 11, 12}
print(diff3)


setA.intersection_update(setB)    #  Vypíše pouze opakující se hodnoty v obou setech {1, 2, 3}
print(setA)

# Příklad 3
setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
setE = {7, 8}


print(setC.issubset(setD))    # False. issubset nám řekne, zda všechny hodnoty setC se nachází v setD
print(setD.issubset(setC))    # True
print(setD.issuperset(setC))   # False. Protože setD neobsahuje všehny hodnoty ze setC
print(setC.issuperset(setD))   # True
print(setC.isdisjoint(setE))   # True. Isdisjoint nám řekne, zda hodnoty mezi sety se různí
