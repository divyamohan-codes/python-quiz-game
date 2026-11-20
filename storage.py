import json
import os


def load_decks():
    with open("decks.json", "r") as file:
        data = json.load(file)

    return data


def load_progress():
    if not os.path.exists("progress.json"):
        return {}

    with open("progress.json", "r") as file:
        return json.load(file)


def save_progress(progress):
    with open("progress.json", "w") as file:
        json.dump(progress, file, indent=4)


def save_result(name, result):
    progress = load_progress()

    if name not in progress:
        progress[name] = []

    progress[name].append(result)

    save_progress(progress)

def save_deck(deck_name, questions):
    decks = load_decks()

    decks[deck_name] = questions

    with open("decks.json", "w") as file:
        json.dump(decks, file, indent=4)

    print("Deck saved successfully!")
