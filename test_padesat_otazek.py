import random

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

def generate_questions():

    questions = [
    Question("Jak se vytvoří prázdný list v Pythonu?", ["a) []", "b) {}", "c) ()", "d) //"], "a"),
    Question("Jak se přidá prvek do listu v Pythonu?", ["a) list.add(prvek)", "b) list.append(prvek)", "c) list.insert(prvek)", "d) list.extend(prvek)"], "b"),
    Question("Jak vypíšete text na obrazovku v Pythonu?", ["a) print('text')", "b) console.log('text')", "c) echo('text')", "d) printf('text')"], "a"),
    Question("Jak vytvoříte proměnnou v Pythonu?", ["a) new", "b) var", "c) let", "d) žádné z výše uvedených"], "d"),
    Question("Jaký je výsledek výrazu 5 + 3?", ["a) 8", "b) 53", "c) 15", "d) 35"], "a"),
    Question("Co udělá operátor % v Pythonu?", ["a) Dělení", "b) Násobení", "c) Zbytek po dělení", "d) Součet"], "c"),
    Question("Jak vytvoříte smyčku 'for' v Pythonu?", ["a) for i in range(10):", "b) for i = 0; i < 10; i++:", "c) for (int i = 0; i < 10; i++):", "d) for i < 10:"], "a"),
    Question("Jaké je výchozí hodnota pro proměnnou typu int v Pythonu?", ["a) 0", "b) 1", "c) null", "d) 'undefined'"], "a"),
    Question("Jaký je výsledek výrazu 2 ** 3?", ["a) 6", "b) 8", "c) 12", "d) 16"], "b"),
    Question("Co udělá funkce 'len()' v Pythonu?", ["a) Vrátí délku řetězce", "b) Vytvoří nový řetězec", "c) Vrátí první prvek v poli", "d) Zjistí délku listu"], "a"),
    Question("Jakým způsobem se komentuje kód v Pythonu?", ["a) // Komentář", "b) /* Komentář */", "c) # Komentář", "d) <!-- Komentář -->"], "c"),
    Question("Jaké jsou logické operátory v Pythonu?", ["a) &&, ||, !", "b) and, or, not", "c) AND, OR, NOT", "d) and, or, !"], "b"),
    Question("Co vrátí funkce 'int(\"10\")'?", ["a) 10", "b) '10'", "c) 0", "d) Chyba"], "a"),
    Question("Jak získáte podřetězec (substring) v Pythonu?", ["a) str.slice(start, end)", "b) str.substring(start, end)", "c) str.substr(start, length)", "d) str.sub(start, end)"], "c"),
    Question("Jakým způsobem získáte vstup od uživatele v Pythonu?", ["a) input()", "b) read()", "c) get_user_input()", "d) get_input()"], "a"),
    Question("Jak vytvoříte funkci v Pythonu?", ["a) def my_function():", "b) function my_function():", "c) define my_function():", "d) func my_function():"], "a"),
    Question("Co udělá funkce 'range(5)'?", ["a) Vytvoří seznam od 1 do 5", "b) Vytvoří seznam od 0 do 5", "c) Vytvoří seznam od 1 do 4", "d) Vytvoří seznam od 0 do 4"], "d"),
    Question("Jak získáte délku listu v Pythonu?", ["a) list.length()", "b) length(list)", "c) len(list)", "d) count(list)"], "c"),
    Question("Který datový typ se používá pro celá čísla v Pythonu?", ["a) int", "b) float", "c) double", "d) long"], "a"),
    Question("Jaké jsou pravdivostní hodnoty v Pythonu?", ["a) true, false", "b) 1, 0", "c) yes, no", "d) on, off"], "a"),
    Question("Jaký operátor slouží k přiřazení hodnoty proměnné v Pythonu?", ["a) =", "b) :=", "c) ->", "d) -="], "a"),
    Question("Který operátor se používá pro získání zbytku po celočíselném dělení v Pythonu?", ["a) %", "b) //", "c) /", "d) *"], "a"),
    Question("Co udělá funkce 'round(3.14)'?", ["a) 3", "b) 4", "c) 3.1", "d) 3.2"], "a"),
    Question("Který datový typ se používá pro desetinná čísla v Pythonu?", ["a) float", "b) int", "c) double", "d) real"], "a"),
    Question("Jak získáte absolutní hodnotu čísla v Pythonu?", ["a) abs()", "b) absolute()", "c) Math.abs()", "d) Math.absolute()"], "a"),
    Question("Jak získáte poslední prvek v listu v Pythonu?", ["a) list.last()", "b) list[length-1]", "c) list[-1]", "d) list.tail()"], "c"),
    Question("Který operátor se používá pro násobení v Pythonu?", ["a) *", "b) x", "c) •", "d) multiply"], "a"),
    Question("Která klíčová slova se používají pro podmínky v Pythonu?", ["a) if, elif, else", "b) case, when, otherwise", "c) switch, case, default", "d) condition, then, else"], "a"),
    Question("Který datový typ se používá pro textové řetězce v Pythonu?", ["a) str", "b) string", "c) txt", "d) text"], "a"),
    Question("Jak vytvoříte náhodné číslo v Pythonu?", ["a) random.randint(1, 10)", "b) random.random(1, 10)", "c) random.number(1, 10)", "d) random.generate(1, 10)"], "a"),
    Question("Které klíčové slovo se používá pro vystoupení ze smyčky v Pythonu?", ["a) break", "b) stop", "c) exit", "d) end"], "a"),
    Question("Co udělá funkce 'list(range(5))'?", ["a) Vytvoří list [0, 1, 2, 3, 4]", "b) Vytvoří list [1, 2, 3, 4, 5]", "c) Vytvoří list [5, 4, 3, 2, 1]", "d) Vytvoří list [0, 0, 0, 0, 0]"], "a"),
    Question("Jak v Pythonu získáte horní celou část čísla (zaokrouhlení dolů)?", ["a) int(number)", "b) round(number)", "c) ceil(number)", "d) floor(number)"], "a"),
    Question("Jaký je výsledek výrazu 'hello' + 'world'?", ["a) 'hello world'", "b) 'helloworld'", "c) 'hello' + ' ' + 'world'", "d) 'hello' . 'world'"], "a"),
    Question("Který datový typ se používá pro pravdivostní hodnoty v Pythonu?", ["a) bool", "b) boolean", "c) logical", "d) bit"], "a"),
    Question("Jak získáte první prvek v listu v Pythonu?", ["a) list.first()", "b) list[0]", "c) list.head()", "d) list.start()"], "b"),
    Question("Co udělá funkce 'max([3, 6, 1, 9])'?", ["a) Vrátí maximum ze seznamu", "b) Vrátí minimum ze seznamu", "c) Vrátí součet prvků seznamu", "d) Vrátí průměr prvků seznamu"], "a"),
    Question("Jaký je výsledek výrazu 'Python'[-1]?", ["a) 'P'", "b) 'n'", "c) 'o'", "d) 't'"], "d"),
    Question("Který operátor se používá pro dělení v Pythonu?", ["a) /", "b) div", "c) divmod", "d) %"], "a"),
    Question("Jak získáte vstup jako číslo v Pythonu?", ["a) int(input())", "b) input(int)", "c) to_int(input())", "d) int = input()"], "a"),
    Question("Který datový typ se používá pro kolekce unikátních prvků v Pythonu?", ["a) set", "b) list", "c) tuple", "d) dictionary"], "a"),
    Question("Co udělá operátor 'in' v Pythonu?", ["a) Ověří, zda je prvek v kolekci", "b) Vloží prvek do kolekce", "c) Vrátí prvek z kolekce", "d) Odebere prvek z kolekce"], "a"),
    Question("Který operátor se používá pro sčítání v Pythonu?", ["a) +", "b) sum", "c) add", "d) plus"], "a"),
    Question("Která funkce vrací největší hodnotu z několika argumentů v Pythonu?", ["a) max()", "b) maximum()", "c) largest()", "d) top()"], "a"),
    Question("Jak získáte poslední prvek v řetězci v Pythonu?", ["a) str.last()", "b) str[-1]", "c) str.end()", "d) str.tail()"], "b"),
    Question("Která funkce vrací nejmenší hodnotu z několika argumentů v Pythonu?", ["a) min()", "b) minimum()", "c) smallest()", "d) bottom()"], "a"),
    Question("Která funkce vrací zaokrouhlené číslo v Pythonu?", ["a) round()", "b) ceil()", "c) floor()", "d) abs()"], "a"),
    Question("Který operátor se používá pro odčítání v Pythonu?", ["a) -", "b) subtract", "c) minus", "d) sub"], "a"),
    Question("Které klíčové slovo se používá pro vytvoření třídy v Pythonu?", ["a) class", "b) def", "c) function", "d) create"], "a"),
    Question("Jak získáte první prvek v řetězci v Pythonu?", ["a) str.first()", "b) str[0]", "c) str.head()", "d) str.start()"], "b"),
    Question("Co udělá funkce 'sum([1, 2, 3])'?", ["a) Vrátí součet prvků seznamu", "b) Vrátí průměr prvků seznamu", "c) Vrátí maximum ze seznamu", "d) Vrátí minimum ze seznamu"], "a"),
    # ... další otázky ...
]

    return questions

def ask_questions(questions, num_questions):
    random.shuffle(questions)  # Zamíchání otázek

    score = 0

    # Procházení náhodně vybraných otázek
    for i in range(num_questions):
        question = questions[i]
        print(question.text)
        for option in question.options:
            print(option)

        user_answer = input("Vyberte správnou odpověď (a, b, c nebo d): ").lower()

        # Porovnat odpověď uživatele s správnou odpovědí
        if user_answer == question.correct_option:
            print("Správně!")
            score += 1
        else:
            print("Chyba. Správná odpověď byla: " + question.correct_option)

    return score

if __name__ == "__main__":
    # Generování otázek
    questions = generate_questions()

    # Počet otázek
    num_questions = 5  # Změnil jsem na 5 pro účely demonstrace

    print(f"Zodpovězte následujících {num_questions} otázek:")

    # Položení otázek a získání skóre
    score = ask_questions(questions, num_questions)

    # Výsledek testu
    print("Váš výsledek: {}/{}".format(score, num_questions))
