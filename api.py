
from models import Question
import requests
import html
import random


def fetch_questions(amount, difficulty=None):

    url = "https://opentdb.com/api.php"

    params = {
        "amount": amount,
        "type": "multiple"
    }

    if difficulty:
        params["difficulty"] = difficulty

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

        if data["response_code"] != 0:
            print("No questions available. Please try another difficulty.")
            return []

        questions = []

        for item in data["results"]:

            question_text = html.unescape(item["question"])
            correct = html.unescape(item["correct_answer"])

            incorrect = [
                html.unescape(answer)
                for answer in item["incorrect_answers"]
            ]

            choices = incorrect + [correct]

            random.shuffle(choices)

            question = Question(
                text=question_text,
                answer=correct,
                choices=choices)

            questions.append(question)

        return questions

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    except (ValueError, KeyError, TypeError):
        print("Unexpected API response.")

    return []
