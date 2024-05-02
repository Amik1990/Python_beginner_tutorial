# 1. příklad
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input.")


# 2. příklad.  Vylepšená verze. Do kódu vložím dělení nulou což se nesmí. Aby systém na to reagoval, tak upravím kód.
try:
    value = 10 / 0
    number2 = int(input("Enter a number: "))
    print(number2)
except ZeroDivisionError:
    print("Divided by zero.")
except ValueError:
    print("Invalid Input.")

# 3. příklad.  Jiný způsob zápisu. Kdy zerodivisionerror bude jako promenna. Do kódu vložím dělení nulou což se nesmí. 
try:
    value = 10 / 0
    number2 = int(input("Enter a number: "))
    print(number2)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input.")
