# "r" - read,  "w" - write, "a" - append (mohu přidat informaci na konec), "r+"- read and write

# 1. Příklad. Otevře dokument
scratch_file = open("scratch.txt", "r")

# readable nám řekne, zda je dokument scratch čitelný (napíše True nebo False). Pokud bude nastavené něco jiného než "r" tak výjde False.
print(scratch_file.readable())

# read vypíše obsah dokumentu
print(scratch_file.read())

scratch_file.close()


# 2. Pokračování s dokumentem cars. Readable vypíše první řádek v dokumentu. Když ho napíšu znovu, tak vypíše druhý řádek, atd.

cars_file = open("cars.txt", "r")
print(cars_file.readable())

print(cars_file.readline())
print(cars_file.readline())
cars_file.close()


# 3. Readlines vypíše všechny řádky do seznamu, Pokud jsme předtím nepoužili readline.
cars_file = open("cars.txt", "r")
print(cars_file.readable())

print(cars_file.readlines())
cars_file.close()

# 4. Když chci vypsat do seznamu konkrétní řádek, tak dopíšu index [] u readlines
cars_file = open("cars.txt", "r")
print(cars_file.readable())

print(cars_file.readlines()[1])
cars_file.close()

# 5. Použití loop (for funkce) Když chci vypsat všechny značky.
cars_file = open("cars.txt", "r")
for car in cars_file.readlines():
    print(car)
""" mohu napsat i takto
for car in cars_file:
    print(car)
"""
cars_file.close()
