# cube anglicky je mocnina
# První příklad. Pozor, když použiju ve funkci return, tak tímto funkce končí. Další řádky ve funkci se nepropíšou
def cube(num):
    return num*num*num

print(cube(3))

# Další příklad (jiný způsob zápisu s použitím proměnné)
def cube(num):
    return num*num*num

result = cube(4)
print(result)


# Další příklad. Zde se nic nepropíše!!!!!
def cube(num):
    return num*num*num

cube(2)
