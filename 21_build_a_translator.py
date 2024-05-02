
# Překladač: Samohlásky nahradí "g". Výsledek bude napsaný malými písmeny.
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate("To be or not to be"))

# Verze, kdy chci, aby prekladac pozadal uzivatele, aby napsal frázi pro preklad:
print(translate(input("Enter a phrase no.1: ")))


# Jiný způsob zápisu, aby stačilo napsat "aeiou". Samohlásky nahradí "g". Dopsali jsme if podmínky lower, isupper, aby se nám vypisovala velká i malá písmena
def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate2(input("Enter a phrase no.2: ")))
