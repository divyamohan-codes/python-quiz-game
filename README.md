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

Developed as part of the SkillMe Python Virtual Internship – Week 3.# Python Quiz Game

## Project Description
This is a simple Python-based quiz game developed as part of my Python Engineering Internship.The game displays questions from a text file, checks the user's answers, calculates the final score and percentage, and allows the user to replay the quiz.

## Features
- Reads questions from a text file.
- Uses functions to organize the code.
- Checks answers automatically.
- Uses loops to display questions and replay the game.
- Randomizes question order.
- Calculates score and percentage.
- Provides a replay option.

## Technologies Used
- Python
- VS Code
- File Handling

## Project Files
- quiz_game.py – Main Python program.
- questions.txt – Stores quiz questions and answers.
- README.md – Project documentation.

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the command:

   py quiz_game.py

5. Answer the questions and enjoy the quiz!

## Learning Outcomes
Through this project, I practised Python functions, loops, conditional statements, file handling, lists and randomization.

---

## Week 2 – QuizCraft: Organized Quiz System

### New Features
- Organized questions into different decks.
- Used Python classes to manage questions and quiz sessions.
- Added multiple-choice quiz functionality.
- Added player name support.
- Stored quiz progress using JSON files.
- Added a statistics menu to track quiz performance.
- Saved progress even after closing the program.

### Technologies Used
- Python
- Object-Oriented Programming (OOP)
- JSON
- VS Code

### Project Files
- `main.py` – Main program
- `models.py` – Classes for quiz management
- `storage.py` – Handles saving and loading data
- `decks.json` – Stores quiz decks
- `progress.json` – Stores player progress

### How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

### Learning Outcomes
- Understanding Python classes and objects.
- Organizing code into multiple files.
- Working with JSON data.
- Building a structured quiz application.

  ---

## Week 3 – QuizCraft: API Integration

### Project Description

In Week 3, QuizCraft was enhanced by integrating the Open Trivia Database (OpenTDB) API. This allows users to fetch fresh multiple-choice questions from an online source instead of depending only on locally stored questions.

### New Features

- Integrated the Open Trivia Database API to fetch online questions.
- Allowed users to select the number of questions.
- Added difficulty-level selection.
- Retrieved multiple-choice questions with answer options.
- Shuffled answer choices randomly.
- Processed API responses using JSON.
- Handled HTML-encoded text in API responses.
- Added error handling for network issues and API request failures.
- Supported saving online questions as local decks.
- Allowed saved decks to be played offline.

### Technologies Used

- Python
- Requests library
- REST API
- JSON
- Open Trivia Database (OpenTDB)
- Exception Handling

### Project Files

- `main.py` – Main application and quiz menu.
- `models.py` – Defines classes for questions, decks and quiz sessions.
- `storage.py` – Handles saving and loading quiz decks and progress.
- `api.py` – Fetches questions from the OpenTDB API.
- `check_api.py` – Checks whether API questions can be fetched.
- `test_api.py` – Used for API testing.
- `decks.json` – Stores local question decks.
- `progress.json` – Stores quiz progress.

### How to Run

1. Install Python.
2. Install the required library:

   `python -m pip install requests`

3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

   `python main.py`

### API Used

Open Trivia Database: https://opentdb.com/

### Learning Outcomes

- Understanding REST API integration.
- Sending HTTP requests using the Requests library.
- Retrieving and processing JSON data.
- Working with external APIs.
- Understanding exception handling and network errors.
- Organizing a Python project into multiple modules.
- Building an application that supports both online and offline quizzes.

### Internship

Developed as part of the SkillMe Python Virtual Internship – Week 3.
