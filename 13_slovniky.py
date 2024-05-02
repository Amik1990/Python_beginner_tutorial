
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
     4: "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octomber",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions[4])

# jiný způsob zápisu. Používá se, když chci, aby se mi zobrazil defaultni klíč, když zapíšu chybný klíč
print(monthConversions.get("Vut", "Not a valid key"))

#  Slovník z více typů hodnot:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

#  Další způsob jak definovat slovník:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Vypíše hodnotu klíče model:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# x = thisdict.get("model")     jiný způsob zápisu
print(x)

#  Vypís klíčů:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()
print(x)


# Přídání klíče a hodnoty do slovníku:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#  Výpis hodnot:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()
print(x)

#  Vypíše obsah slovníku ve formátu tuple:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()
print(x)


# Použití update pro změnu roku:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)


#  Vypíše klíče pomocí for metody:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

# jiný způsob zápisu
# for x in thisdict.keys():
#   print(x)


# Vypíše hodnoty slovníku pomocí for:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

# jiný způsob zápisu
# for x in thisdict.values():
#   print(x)


#  Vypíše klíče i hodnoty:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

