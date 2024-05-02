import random

def generate_questions():
    questions = {
        "Jak se vytvoří prázdný list v Pythonu?": "[]",
        "Jak se přidá prvek do listu v Pythonu?": "list.append(prvek)",
        "Jak vypíšete text na obrazovku v Pythonu?": "print('text')",
        # Přidat další otázky a odpovědi podle potřeby
    }
    return questions

def ask_questions(questions, num_questions):
    keys = list(questions.keys())
    random.shuffle(keys)  # Zamíchání otázek

    score = 0

    # Procházení náhodně vybraných otázek
    for i in range(num_questions):
        question = keys[i]
        correct_answer = questions[question]

        user_answer = input(question + "\nOdpověď: ")

        # Porovnat odpověď uživatele s správnou odpovědí
        if user_answer.strip().lower() == correct_answer.lower():
            print("Správně!")
            score += 1
        else:
            print("Chyba. Správná odpověď je:", correct_answer)

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
