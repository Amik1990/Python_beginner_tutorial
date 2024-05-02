# Kalkulačka

# Když zadám 2 a 7, tak mi nevýjde 9, ale 27. Vypíše čísla vedle sebe.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = (num1 + num2)
print(result)

# Aby to fungovalo, tak string musím převést na integer. Pozor funguje pouze pro celá čísla.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
