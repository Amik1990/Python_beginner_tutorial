# 1. příklad.
is_male = True

if is_male:
    print("You are a male")

# 2. příklad. Nic nevypíše, protože jeto False
is_male = False

if is_male:
    print("You are a male")

# 3 příklad
is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")


# 4. příklad. Else se propíše pouze pokud obě proměnné jsou False.If se propíše tehdy ,kdy alespon jedna promenna je True

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


# 5. příklad. Else se propíše když alespoň jedna proměnna je False.If se propíše tehdy ,kdy obě promenné jsou True

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall ")
else:
    print("You are either not male or not tall or both")


# 6. příklad. If se propíše tehdy ,kdy obě promenné jsou True. Elif se propíše, když is_male je True a is_tall je False.

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall ")
elif is_male and not(is_tall):
    print("You are a male and not tall")
else:
    print("You are either not male or not tall or both")


# 7. příklad. If se propíše tehdy ,kdy obě promenné jsou True.

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male and tall ")
elif is_male and not(is_tall):
    print("You are a male and not tall")
elif not(is_male) and is_tall:
    print("You are not male and you are tall")
else:
    print("You are not a male not tall")
