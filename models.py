
class Question:
    def __init__(self, text, answer, choices=None):
        self.text = text
        self.answer = answer
        self.choices = choices

    def check(self, user_answer):
        return user_answer.strip().lower() == self.answer.lower()


class Deck:
    def __init__(self, name, questions):
        self.name = name
        self.questions = []

        for item in questions:
            question = Question(
                item["text"],
                item["answer"],
                item.get("choices")
            )
            self.questions.append(question)


class QuizSession:
    def __init__(self, deck):
        self.deck = deck
        self.score = 0

    def play(self):
        for question in self.deck.questions:
            print("\n" + question.text)

            if question.choices:
                for i, choice in enumerate(question.choices):
                    print(f"{chr(65 + i)}) {choice}")

                user_answer = input("Enter your option (A/B/C/D): ")

                if user_answer.upper() in ["A", "B", "C", "D"]:
                    index = ord(user_answer.upper()) - 65
                    if index < len(question.choices):
                        user_answer = question.choices[index]
            else:
                user_answer = input("Your answer: ")

            if question.check(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

        return {
            "deck": self.deck.name,
            "score": self.score,
            "total": len(self.deck.questions)
        }
