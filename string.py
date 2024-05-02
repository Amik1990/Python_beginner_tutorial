
my_string ="Hello World"
print(my_string.replace("World", "Universe"))   # Hello Universe

my_string = "how are you doing"
my_list = my_string.split()   # v závorce u split metody je defaultně mezera. Tzn. rozdělí v místě mezery
print(my_list)    # ['how', 'are', 'you', 'doing']

my_string = "how,are,you,doing"    # zde mezera není, proto vypíše jako jednu hodnotu seznamu
my_list = my_string.split()
print(my_list)   #  ['how,are,you,doing']

my_string = "how,are,you,doing"    # Aby se slova vypsala jako samostatné hodnoty , tak musíme do závorky napsat čárku
my_list = my_string.split(",")
print(my_list)   #  [' how', 'are', 'you', 'doing']

my_string = "how,are,you,doing"
my_list = my_string.split(",")
new_string = "".join(my_list)    # sečte
print(new_string)  # howareyoudoing


my_string = "how,are,you,doing"
my_list = my_string.split(",")
new_string = " ".join(my_list)    # sečte
print(new_string)  # how are you doing


my_list = ["a"] * 6
print(my_list)   # ['a', 'a', 'a', 'a', 'a', 'a']
my_string = "".join(my_list)  # hodnoty listu pomocí .join vypíšeme jako string
print(my_string)   #  aaaaaa
