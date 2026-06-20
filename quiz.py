questions = ("How many elements are there in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What is the most abundant gas in the atmosphere?: ",
             "How many bones are there in the human body?: ",
             "Which is the hottest planet in the solar system?: ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f" {answers[question_num]} is the correct answer")
    question_num += 1


print("---------------------------")
print("          RESULT           ")
print("---------------------------")
print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"ypur score is{score}%")