import random
def read_questions():
    questions=[]
    file=open("questions.txt","r")
    for line in file:
        question, answer = line.strip().split("|")
        questions.append((question,answer))
    file.close()
    return questions
def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True   
    else:
        print("Wrong answer!")
        print("Correct answer:", correct_answer)
        return False
def play_quiz():
    questions = read_questions()
    random.shuffle(questions)
    score = 0
    for question, answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ")
        if check_answer(user_answer, answer):
            score += 1
    total=len(questions)
    percentage = (score / total) * 100
    print("\nQuiz completed!")
    print("Your score:", score, "/", total)
    print("Percentage:", percentage, "%")
def main():
    while True:
        play_quiz()
        choice = input("\nDo you want to play again? (yes/no): ")
        if choice.lower() != "yes":
            print("Thank you for playing!")
            break
main()