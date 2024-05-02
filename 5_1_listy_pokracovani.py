
# Vložení hodnoty na třetí pozici:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Přidání hodnoty na konec seznamu:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Rozšíření seznamu o další seznam. Mohu rozěířit i o tuple nebo slovník.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Odstranění banana ze seznamu. Pokud se banana vyskytuje víckrát, tak se vymaže první v seznamu.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Odstranění hodnoty seznamu dle indexu.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Vymazání poslední hodnoty:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#  Vymazání hodnoty pomocí remove:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#  Vymazání obsahu seznamu. Zůstane prázdný seznam.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Seřazení obsahu alfabeticky
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Zkopírování seznamu:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#  Jiný způsob kopírování seznamu:      Zde ale pozor. Když změním  mylist, tak se změní i původní seznam!!!
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
