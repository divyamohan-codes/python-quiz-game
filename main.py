from models import Deck, QuizSession
from storage import load_decks, save_result, load_progress, save_deck
from api import fetch_questions
from datetime import datetime
def online_quiz(name):
    print("\n--- ONLINE QUIZ ---")

    try:
        amount = int(input("How many questions do you want? "))

        if amount < 1 or amount > 10:
            print("Please choose between 1 and 10 questions.")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty!")
        return

    questions = fetch_questions(amount, difficulty)

    if not questions:
        print("Online quiz unavailable. Please try a local deck instead.")
        return

    question_data = []

    for q in questions:
        question_data.append({
            "text": q.text,
            "answer": q.answer,
            "choices": q.choices
        })

    deck = Deck("Online Quiz", question_data)
    session = QuizSession(deck)

    result = session.play()
    result["date"] = datetime.now().isoformat()
    save_result(name, result)

    print(f"\nYour score: {result['score']}/{result['total']}")

    save_choice = input("Do you want to save these questions as a new deck? (yes/no): ").lower()

    if save_choice == "yes":
        deck_name = input("Enter a name for your deck: ").strip()

        if deck_name:
            save_deck(deck_name, question_data)
        else:
            print("Deck name cannot be empty!")


def show_stats(name):
    progress = load_progress()

    if name not in progress or not progress[name]:
        print("No quiz attempts yet!")
        return

    print("\n--- YOUR QUIZ STATS ---")

    for deck_name in set(item["deck"] for item in progress[name]):
        attempts = [
            item for item in progress[name]
            if item["deck"] == deck_name
        ]

        best = max(item["score"] for item in attempts)

        print(f"\nDeck: {deck_name}")
        print(f"Attempts: {len(attempts)}")
        print(f"Best score: {best}/{attempts[0]['total']}")


def main():
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    while True:
        print("\n===== QUIZCRAFT =====")
        print("1. Play Local Quiz")
        print("2. Play Online Quiz")
        print("3. View Stats")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            decks_data = load_decks()
            deck_names = list(decks_data.keys())

            print("\nAvailable Decks:")

            for i, deck_name in enumerate(deck_names, 1):
                print(f"{i}. {deck_name}")

            try:
                selected = int(input("Choose a deck: "))

                if selected < 1 or selected > len(deck_names):
                    print("Invalid deck choice!")
                    continue

                deck_name = deck_names[selected - 1]
                deck = Deck(deck_name, decks_data[deck_name])

                session = QuizSession(deck)
                result = session.play()

                result["date"] = datetime.now().isoformat()
                save_result(name, result)

                print(f"\nYour score: {result['score']}/{result['total']}")

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            online_quiz(name)

        elif choice == "3":
            show_stats(name)

        elif choice == "4":
            print("Thank you for playing QuizCraft!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

