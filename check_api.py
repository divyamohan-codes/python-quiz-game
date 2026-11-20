
from api import fetch_questions

questions = fetch_questions(5)

for q in questions:
    print("\nQuestion:", q.text)
    print("Choices:", q.choices)
    print("Answer:", q.answer)
