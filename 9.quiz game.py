questions = ("how many element in PD table?: ",
            "which animal lays the largest egg?: ",
            "what is your name?:",
            "what is your age?:")
options = (("A.116", "B.117", "C.118","D.119"),
           ("A.whale", "B.croc", "C.elephant","D.ostrich"),
           ("A.pall", "B.jack", "C.zoey","D.sam"),
           ("A.20", "B.12", "C.27","D.45"))
answers = ("A", "D", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Answer : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"Answer {answers[question_num]} is the correct answer")
    question_num += 1

print("----------------")
print("Answer" , end=' ')
for answer in answers:
    print(answer, end=' ')
print()
print("Guess" , end=' ')
for guess in guesses:
    print(guess, end= ' ')
print()
score = int(score / len(questions) * 100)
print(f"Your score is {score}%")

