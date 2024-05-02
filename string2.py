from timeit import default_timer as timer

# Příklad jak vypsat hondoty slovníku do stringu. Použití .join metody
my_list = ["a"] * 100000
# print(my_list)   # ['a', 'a', 'a', 'a', 'a', 'a']

# efektivní varianta
start = timer()
my_string = "".join(my_list)  # hodnoty listu pomocí .join vypíšeme jako string
stop = timer()
# print(my_string)   #  aaaaaa
print(stop-start)

# alternativní možnost, ale špatná varianta (bere výpočetní výkon)
start = timer()
my_string1 = ""
for i in my_list:
    my_string1 += i
stop = timer()
# print(my_string)
print(stop-start)
