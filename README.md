# QuizCraft – Flashcard & Quiz Trainer

A Python-based quiz application developed as part of my SkillMe Python Virtual Internship.

## Features

- Play quizzes using local question decks.
- Organize questions into different categories such as Python and DSA.
- Fetch new multiple-choice questions using the Open Trivia Database API.
- Select the number of questions and difficulty level.
- Shuffle answer options randomly.
- View quiz scores and track progress.
- Save online questions as new local decks.
- Play saved decks offline.
- Handle API errors, network issues and request timeouts.

## Technologies Used

- Python
- Requests library
- JSON
- Open Trivia Database API

## Project Files

- `main.py` – Main application and menu.
- `models.py` – Question, Deck and QuizSession classes.
- `storage.py` – Saves and loads decks and quiz progress.
- `api.py` – Fetches online quiz questions.
- `decks.json` – Stores local question decks.
- `progress.json` – Stores quiz results.

## Installation

Install the required library:

```bash
python -m pip install requests
```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

## API Used

Open Trivia Database: https://opentdb.com/

## Learning Outcomes

- Understanding Python functions and classes.
- Working with REST APIs.
- Handling JSON responses.
- Using external Python libraries.
- Implementing exception handling.
- Managing data using JSON files.

## Internship

Developed as part of the SkillMe Python Virtual Internship – Week 3.