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
        Question("Jak vypíšete text na obrazovku v Pythonu?", ["a) print('text')", "b) console.log('text')", "c) echo('text')", "d) printf('text')"], "a")
        # Přidat další otázky a odpovědi podle potřeby
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

        user_answer = input("Vyberte správnou možnost (a, b, c nebo d): ").lower()

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
    num_questions = 3  # Změnil jsem na 3 pro účely demonstrace

    print(f"Zodpovězte následujících {num_questions} otázek:")

    # Položení otázek a získání skóre
    score = ask_questions(questions, num_questions)

    # Výsledek testu
    print("Váš výsledek: {}/{}".format(score, num_questions))
